#!/bin/bash

# Exit immediately if any command fails
set -e

# Run black
poetry run black --check *.py

# Run isort
poetry run isort --check *.py

# Run flake8, ignoring test.py (cannot enforce line length with URLS)
poetry run flake8 --exclude=test.py *.py