#!/bin/bash

# Load environment variables from .env file
set -a
source .env
set +a

# Rsync command
rsync -avz --progress "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}" "${LOCAL_PATH}"
