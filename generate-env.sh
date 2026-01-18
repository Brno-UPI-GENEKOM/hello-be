#!/bin/bash
# Check if the folder exists, create it if not
mkdir -p dist/hello-fe/browser/assets
# Write the variable to the file
echo "window.env = { BACKEND_URL: '${BACKEND_URL}' };" > dist/hello-fe/browser/assets/env.js