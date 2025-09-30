#!/usr/bin/env bash
set -eo pipefail

COLOR_GREEN='\033[0;32m'
COLOR_RED='\033[0;31m'
COLOR_NC='\033[0m'

echo "starting black"
poetry run black .
echo "OK"

echo "Starting ruff"
poetry run ruff check --select I --fix
poetry run ruff check --fix
echo "OK"

echo "Starting mypy"
poetry run mypy .
echo "OK"

echo "STarting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "${COLOR_GREEN}ALL tests passed successfully!${COLOR_NC}"