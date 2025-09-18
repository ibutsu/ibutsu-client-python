#!/usr/bin/env bash
set -euo pipefail
####
# Re-generate the client based on the spec

# Configuration
OPENAPI_GENERATOR_VERSION="7.15.0"
CLIENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TEMP_DIR="${CLIENT_DIR}/tmp/client"
OPENAPI_FILE=""
CAN_COMMIT=false
CAN_PUSH=false
CAN_DELETE=false

# Version extraction function
get_versions() {
    CURRENT_VERSION=$(hatch version 2>/dev/null || python3 -c "
try:
    import tomllib
    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)
    print(data.get('project', {}).get('version', '0.0.1'))
except:
    print('0.0.1')
" 2>/dev/null || echo "0.0.1")

    if [[ "${NEW_VERSION:-}" == "" ]]; then
        # If there's no new version defined externally, generate a new version
        # Handle version formats like "2.3.0" or "2.3.0.d20250918"
        if [[ "$CURRENT_VERSION" =~ ^([0-9]+\.[0-9]+\.[0-9]+) ]]; then
            BASE_VERSION="${BASH_REMATCH[1]}"
            PATCH_VERSION="${BASE_VERSION##*.}"
            NEW_PATCH=$((PATCH_VERSION + 1))
            NEW_VERSION="${BASE_VERSION%.*}.$NEW_PATCH"
        else
            # Fallback for unexpected version formats
            NEW_VERSION="2.3.1"
        fi
    fi
}

# Clean up .openapi-generator folder if version upgrade detected
function cleanup_openapi_generator_folder() {
    local old_version_file="${CLIENT_DIR}/.openapi-generator/VERSION"

    if [[ -f "$old_version_file" ]]; then
        local old_version=$(cat "$old_version_file" 2>/dev/null || echo "unknown")
        echo "Previous OpenAPI Generator version: $old_version"
        echo "New OpenAPI Generator version: $OPENAPI_GENERATOR_VERSION"

        # Extract major versions for comparison
        local old_major=$(echo "$old_version" | cut -d. -f1)
        local new_major=$(echo "$OPENAPI_GENERATOR_VERSION" | cut -d. -f1)

        if [[ "$old_major" != "$new_major" ]] || [[ "$old_version" == "unknown" ]]; then
            echo "Major version change detected ($old_version -> $OPENAPI_GENERATOR_VERSION)"
            echo "Cleaning up .openapi-generator folder for fresh generation..."
            rm -rf "${CLIENT_DIR}/.openapi-generator"
            echo "✓ .openapi-generator folder cleaned"
        else
            echo "Minor version update, keeping .openapi-generator folder for incremental updates"
        fi
    else
        echo "No previous .openapi-generator/VERSION found, will generate fresh"
    fi
}

# Check dependencies
function check_dependencies() {
    if ! command -v podman >/dev/null 2>&1; then
        echo "Error: Podman is required for consistent OpenAPI generation"
        echo "Please install Podman from https://podman.io/getting-started/installation"
        exit 1
    fi
    if ! command -v hatch >/dev/null 2>&1; then
        echo "Warning: hatch not found, using fallback version detection"
    fi
}

function print_usage() {
    echo "Usage: regenerate-client.sh [-h|--help] [-c|--commit] [-p|--push] [-d|--delete] OPENAPI_FILE"
    echo ""
    echo "optional arguments:"
    echo "  -h, --help       show this help message"
    echo "  -v, --version    show the prospective new version number"
    echo "  -c, --commit     create a new branch and commit all the changes"
    echo "  -p, --push       push the branch up to origin after commit"
    echo "  -d, --delete     delete the branch after pushing"
    echo ""
    echo "Requirements:"
    echo "  - Podman (for consistent OpenAPI generation)"
    echo "  - hatch (recommended for version management)"
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
        -c|--commit)
            CAN_COMMIT=true
            shift
            ;;
        -p|--push)
            CAN_PUSH=true
            shift
            ;;
        -d|--delete)
            CAN_DELETE=true
            shift
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

# Clean up .openapi-generator folder if major version upgrade
cleanup_openapi_generator_folder

# Generate the client using Podman
echo "Generating client with OpenAPI Generator v${OPENAPI_GENERATOR_VERSION}..."
mkdir -p "$(dirname "${TEMP_DIR}")"

podman run --rm \
    -v "${CLIENT_DIR}:/local" \
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
    -p pythonVersion=3.8 \
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
# Remove old generated content but preserve important directories and files
find "${CLIENT_DIR}" -mindepth 1 -maxdepth 1 \
    ! -name '.git' \
    ! -name '.github' \
    ! -name '.ibutsu-env' \
    ! -name 'regenerate-client.sh' \
    ! -name 'LICENSE' \
    ! -name 'tmp' \
    -exec rm -rf {} +

# Copy new generated content
cp -r "${TEMP_DIR}"/. "${CLIENT_DIR}/"

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

# Commit everything
if [[ "$CAN_COMMIT" = true ]]; then
    echo "Committing changes..."
    BRANCH_NAME="regenerate-$NEW_VERSION"

    # Create and switch to new branch
    git checkout -b "$BRANCH_NAME" > /dev/null 2>&1
    git add . > /dev/null 2>&1
    git commit -q -m "Regenerate client with OpenAPI Generator v${OPENAPI_GENERATOR_VERSION}

- Updated to OpenAPI Generator v${OPENAPI_GENERATOR_VERSION}
- Generated client for API version ${NEW_VERSION}
- Removed Travis CI references
- Improved Podman-based generation
- Clean .openapi-generator folder on major version upgrades"

    echo "✓ New branch created and committed: $BRANCH_NAME"

    if [[ "$CAN_PUSH" = true ]]; then
        echo "Pushing to origin/$BRANCH_NAME..."
        git push -q origin "$BRANCH_NAME"
        echo "✓ Branch pushed to origin"

        # Switch back to main/master
        git checkout main 2>/dev/null || git checkout master 2>/dev/null

        if [[ "$CAN_DELETE" = true ]]; then
            git branch -D "$BRANCH_NAME"
            echo "✓ Local branch $BRANCH_NAME deleted"
        fi
    fi
fi

echo ""
echo "🎉 Client regeneration completed successfully!"
echo "   Version: $NEW_VERSION"
echo "   OpenAPI Generator: v$OPENAPI_GENERATOR_VERSION"
if [[ "$CAN_COMMIT" = true ]]; then
    echo "   Branch: $BRANCH_NAME"
fi
