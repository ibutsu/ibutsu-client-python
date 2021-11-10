#!/usr/bin/env bash
####
# Re-generate the client based on the spec

CLIENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
OPENAPI_FILE=""
CAN_COMMIT=false
CAN_PUSH=false
CAN_DELETE=false
CURRENT_VERSION=`cat setup.py | grep 'VERSION =' | cut -d\" -f2`
if [[ "$NEW_VERSION" == "" ]]; then
    # If there's no new version defined externally, generate a new version
    NEW_VERSION="${CURRENT_VERSION%.*}.$((${CURRENT_VERSION##*.}+1))"
fi
FIXES_DIFF='diff --git a/ibutsu_client/api/widget_api.py b/ibutsu_client/api/widget_api.py
index 0f64c89..b888879 100644
--- a/ibutsu_client/api/widget_api.py
+++ b/ibutsu_client/api/widget_api.py
@@ -22,7 +22,6 @@ from ibutsu_client.model_utils import (  # noqa: F401
     validate_and_convert_types
 )
 from ibutsu_client.model.widget_type_list import WidgetTypeList
-from ibutsu_client.model.str_bool_date_datetime_dict_float_int_list_str_none_type import StrBoolDateDatetimeDictFloatIntListStrNoneType
 
 
 class WidgetApi(object):
'


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
}

# Check if there were no arguments
if [[ $# -eq 0 ]]; then
    echo "No arguments supplied"
    print_usage
    exit 127
fi

# Parse the arguments
for ARG in $*; do
    if [[ "$ARG" == "-c" ]] || [[ "$ARG" == "--commit" ]]; then
        CAN_COMMIT=true
    elif [[ "$ARG" == "-p" ]] || [[ "$ARG" == "--push" ]]; then
        CAN_PUSH=true
    elif [[ "$ARG" == "-d" ]] || [[ "$ARG" == "--delete" ]]; then
        CAN_DELETE=true
    elif [[ "$ARG" == "-v" ]] || [[ "$ARG" == "--version" ]]; then
        echo "Prospective version number: $NEW_VERSION"
        exit 0
    elif [[ "$ARG" == "-h" ]] || [[ "$ARG" == "--help" ]]; then
        print_usage
        exit 0
    else
        OPENAPI_FILE=$ARG
    fi
done

# Check if the files exist
if [[ ! $OPENAPI_FILE == http* ]] && [[ ! -f "$OPENAPI_FILE" ]]; then
    echo "Error: No OpenAPI file or incorrect path to file"
    exit 1
fi
if [[ ! -x "$(command -v openapi-generator-cli)" ]]; then
    echo "Error: openapi-generator-cli is not installed. Please see https://openapi-generator.tech/"
    exit 2
fi

# Generate the client
echo -n "Generating client..."
openapi-generator-cli generate -o /tmp/client -g python --package-name ibutsu_client \
    --git-repo-id ibutsu-client-python --git-user-id ibutsu \
    --global-property skipFormModel=true -p packageVersion=$NEW_VERSION \
    -p packageUrl=https://github.com/ibutsu/ibutsu-client-python \
    -i $OPENAPI_FILE > $CLIENT_DIR/generate.log 2>&1
if [ $? -ne 0 ]; then
    echo "error"
    echo "Error: Generating client failed. Please see $CLIENT_DIR/generate.log for errors"
    exit 3
fi
echo "done"

# Modify various files
cat <<EOF >> /tmp/client/.gitignore

# Virtual environment
.ibutsu-env
EOF
rm /tmp/client/git_push.sh
echo "$FIXES_DIFF" | patch -p 1 -d /tmp/client

# Copy all the files
find $CLIENT_DIR -not -path $CLIENT_DIR -not -path "$CLIENT_DIR/.git/*" -not -name '.git' \
    -not -path "$CLIENT_DIR/.github/*" -not -name '.github' \
    -not -path "$CLIENT_DIR/.ibutsu-env/*" -not -name '.ibutsu-env' \
    -not -name 'regenerate-client.sh' -not -name 'LICENSE' \
    -exec rm -fr {} +
cp -r /tmp/client/. $CLIENT_DIR

# Clean up afterward
rm -fr /tmp/client

# Commit everything
if [[ "$CAN_COMMIT" = true ]]; then
    echo -n "Committing code..."
    BRANCH_NAME="regenerate-$NEW_VERSION"
    git checkout -b $BRANCH_NAME > /dev/null 2>&1
    git add . > /dev/null 2>&1
    git commit -q -m "Regenerated client"
    echo "done, new branch created: $BRANCH_NAME"
    if [[ "$CAN_PUSH" = true ]]; then
        echo -n "Pushing up to origin/$BRANCH_NAME..."
        git push -q origin $BRANCH_NAME 
        git checkout master
        if [[ "$CAN_DELETE" = true ]]; then
            git branch -D $BRANCH_NAME
            echo "Deleted branch $BRANCH_NAME"
        fi
    fi
fi
