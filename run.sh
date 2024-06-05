#!/bin/bash

# Load environment variables from .env file
set -o allexport
source .env
set +o allexport
docker pull sweagent/swe-agent-run:latest
docker-compose up --build