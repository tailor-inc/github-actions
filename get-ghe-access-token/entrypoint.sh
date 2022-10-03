#!/bin/bash

output=$(python3 /app/get_access_token.py)
echo "::set-output name=access_token::$output"

