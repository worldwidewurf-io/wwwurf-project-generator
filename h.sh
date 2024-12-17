#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "Testing WWWURF Project Generator locally..."

TEST_DIR=$(mktemp -d)
echo "Created temporary directory: $TEST_DIR"

ORIG_DIR=$(pwd)

cleanup() {
    cd "$ORIG_DIR"
    rm -rf "$TEST_DIR"
    echo "Cleaned up test directory"
}

trap cleanup EXIT

echo "Installing package..."
poetry install

echo "Running tests..."
poetry run pytest

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Tests passed!${NC}"
else
    echo -e "${RED}Tests failed!${NC}"
    exit 1
fi

cd "$TEST_DIR"
echo "Testing project creation..."
PYTHONPATH="$ORIG_DIR" python3 -c "from wwwurf_project_generator.cli import main; main()" create test-project --packages core api

if [ -d "test-project" ]; then
    echo -e "${GREEN}Project created successfully!${NC}"
    
    # Test package structure
    if [ -d "test-project/packages/core" ] && [ -d "test-project/packages/api" ]; then
        echo -e "${GREEN}Package structure verified!${NC}"
    else
        echo -e "${RED}Package structure verification failed!${NC}"
        exit 1
    fi
else
    echo -e "${RED}Project creation failed!${NC}"
    exit 1
fi

cd test-project
echo "Testing package addition..."
PYTHONPATH="$ORIG_DIR" python3 -c "from wwwurf_project_generator.cli import main; main()" add-package new-package

if [ -d "packages/new-package" ]; then
    echo -e "${GREEN}New package added successfully!${NC}"
else
    echo -e "${RED}Package addition failed!${NC}"
    exit 1
fi

echo -e "${GREEN}All local tests completed successfully!${NC}"