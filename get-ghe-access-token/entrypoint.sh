#!/bin/bash

set -eu

output=$(python3 /app/get_access_token.py)
echo "access_token=$output" >> $GITHUB_OUTPUT
