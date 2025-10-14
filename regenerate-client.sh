#!/usr/bin/env bash
set -euo pipefail
####
# Re-generate the client based on the spec

# Configuration
OPENAPI_GENERATOR_VERSION="7.16.0"
CLIENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TEMP_DIR="${CLIENT_DIR}/tmp/client"
OPENAPI_FILE=""

# Version extraction function
get_versions() {
    # Use hatch to get the current version - fail if hatch is not available or can't read version
    if ! command -v hatch >/dev/null 2>&1; then
        echo "Error: hatch is required to read the project version"
        echo "Please install hatch: pip install hatch"
        exit 1
    fi

    CURRENT_VERSION=$(hatch version 2>/dev/null)
    if [[ $? -ne 0 ]] || [[ -z "$CURRENT_VERSION" ]]; then
        echo "Error: Failed to read version using 'hatch version'"
        echo "Make sure you're in the project root and hatch is properly configured"
        exit 1
    fi

    if [[ "${NEW_VERSION:-}" == "" ]]; then
        # If there's no new version defined externally (e.g., via --target-version), generate a new version
        # Handle version formats like "2.3.0" or "2.3.0.d20250918"
        if [[ "$CURRENT_VERSION" =~ ^([0-9]+\.[0-9]+\.[0-9]+) ]]; then
            BASE_VERSION="${BASH_REMATCH[1]}"
            PATCH_VERSION="${BASE_VERSION##*.}"
            NEW_PATCH=$((PATCH_VERSION + 1))
            NEW_VERSION="${BASE_VERSION%.*}.$NEW_PATCH"
        else
            echo "Error: Unexpected version format: $CURRENT_VERSION"
            exit 1
        fi
    else
        # Validate the provided target version format
        if ! [[ "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
            echo "Error: Invalid version format '$NEW_VERSION'. Expected format: X.Y.Z (e.g., 3.0.0)"
            exit 1
        fi
        echo "Using specified target version: $NEW_VERSION"
    fi
}

# Check dependencies
function check_dependencies() {
    if ! command -v podman >/dev/null 2>&1; then
        echo "Error: Podman is required for consistent OpenAPI generation"
        echo "Please install Podman from https://podman.io/getting-started/installation"
        exit 1
    fi
    # Note: hatch requirement is checked in get_versions() function
}

function print_usage() {
    echo "Usage: regenerate-client.sh [-h|--help] [-v|--version] [--target-version VERSION] OPENAPI_FILE"
    echo ""
    echo "optional arguments:"
    echo "  -h, --help                   show this help message"
    echo "  -v, --version                show the prospective new version number"
    echo "  --target-version VERSION     specify a target version (e.g., 3.0.0)"
    echo ""
    echo "This script regenerates the client on the current branch and leaves"
    echo "uncommitted changes in the working tree after running pre-commit."
    echo ""
    echo "Requirements:"
    echo "  - Podman (for consistent OpenAPI generation)"
    echo "  - hatch (required for version management)"
}

# Check if there were no arguments
if [[ $# -eq 0 ]]; then
    echo "No arguments supplied"
    print_usage
    exit 127
fi

# Parse the arguments
while (( "$#" )); do
    case "$1" in
        -h|--help)
            print_usage
            exit 0
            ;;
        -v|--version)
            get_versions
            echo "Current version: $CURRENT_VERSION"
            echo "Prospective version number: $NEW_VERSION"
            exit 0
            ;;
        --target-version)
            if [[ -n "$2" && "$2" != -* ]]; then
                NEW_VERSION="$2"
                shift 2
            else
                echo "Error: --target-version requires a version number argument" >&2
                exit 1
            fi
            ;;
        -*|--*)
            echo "Error: unsupported option $1" >&2
            exit 1
            ;;
        *)
            OPENAPI_FILE=$1
            shift
            ;;
    esac
done

# Initialize versions
get_versions

# Check dependencies
check_dependencies

# Check if the OpenAPI file exists
if [[ ! $OPENAPI_FILE == http* ]] && [[ ! -f "$OPENAPI_FILE" ]]; then
    echo "Error: No OpenAPI file or incorrect path to file"
    exit 1
fi

# Generate the client using Podman
echo "Generating client with OpenAPI Generator v${OPENAPI_GENERATOR_VERSION}..."
mkdir -p "$(dirname "${TEMP_DIR}")"

podman run --rm \
    -v "${CLIENT_DIR}:/local:Z" \
    "openapitools/openapi-generator-cli:v${OPENAPI_GENERATOR_VERSION}" \
    generate \
    -i "/local/${OPENAPI_FILE}" \
    -g python \
    -o "/local/tmp/client" \
    --package-name ibutsu_client \
    --git-repo-id ibutsu-client-python \
    --git-user-id ibutsu \
    --global-property skipFormModel=true \
    -p packageVersion="${NEW_VERSION}" \
    -p packageUrl=https://github.com/ibutsu/ibutsu-client-python \
    -p pythonVersion=3.11 \
    -p generateSourceCodeOnly=false \
    -p library=urllib3 \
    > "${CLIENT_DIR}/generate.log" 2>&1

if [ $? -ne 0 ]; then
    echo "Error: Client generation failed. Please see ${CLIENT_DIR}/generate.log for details"
    exit 3
fi
echo "Client generation completed successfully"

# Clean up and modify generated files
echo "Processing generated files..."

# Remove unwanted generated files
rm -f "${TEMP_DIR}/git_push.sh"
rm -f "${TEMP_DIR}/.travis.yml"

# Add custom .gitignore entries
cat >> "${TEMP_DIR}/.gitignore" << 'EOF'

# Virtual environment
.ibutsu-env
EOF

# Copy generated files while preserving important directories
echo "Copying generated files..."

# Only remove and update the specific directories that contain generated content
echo "Removing old generated content..."
rm -rf "${CLIENT_DIR}/ibutsu_client"
rm -rf "${CLIENT_DIR}/docs"
rm -rf "${CLIENT_DIR}/test"

# Copy only the generated content directories we want to update
echo "Copying new generated content..."
if [[ -d "${TEMP_DIR}/ibutsu_client" ]]; then
    cp -r "${TEMP_DIR}/ibutsu_client" "${CLIENT_DIR}/"
fi
if [[ -d "${TEMP_DIR}/docs" ]]; then
    cp -r "${TEMP_DIR}/docs" "${CLIENT_DIR}/"
fi
if [[ -d "${TEMP_DIR}/test" ]]; then
    cp -r "${TEMP_DIR}/test" "${CLIENT_DIR}/"
fi

# Note: We only copy the specific directories we need (ibutsu_client, docs, test)
# All packaging files (README.md, pyproject.toml, LICENSE, AGENTS.md) are preserved
# We do NOT copy any CI/CD files, setup files, or other generated project files

# Clean up temporary directory
rm -rf "${CLIENT_DIR}/tmp"
echo "File processing completed"

# Post-processing: run formatting and linting if available
echo "Running post-processing..."
if command -v hatch >/dev/null 2>&1; then
    echo "Running code formatting and linting..."
    cd "${CLIENT_DIR}"
    hatch run pre-commit run --all-files || echo "Pre-commit hooks completed with some issues (normal for generated code)"
else
    echo "Hatch not available, skipping code formatting"
fi

echo ""
echo "🎉 Client regeneration completed successfully!"
echo "   Version: $NEW_VERSION"
echo "   OpenAPI Generator: v$OPENAPI_GENERATOR_VERSION"
echo "   Working tree contains uncommitted changes for review"
