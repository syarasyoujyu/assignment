#!/bin/bash

# Load environment variables from .env file
set -o allexport
source .env
set +o allexport

docker-compose up --build