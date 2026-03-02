#!/bin/bash

# 1. Activate the project virtual environment
# This line tries the Windows path first, then the Linux/Mac path
source venv/Scripts/activate || source venv/bin/activate

# 2. Execute the test suite
# Using --headless is best for CI environments
pytest --headless test_app.py

# 3. Capture the exit code
# $? is a special variable that stores the exit status of the last command
if [ $? -eq 0 ]; then
    echo "Tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi