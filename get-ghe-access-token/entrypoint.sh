#!/bin/bash

output=$(python3 get_access_token.py)
echo "::set-output name=access_token::$output"

