#!/bin/bash --login
# Entrypoint for docker container
# The --login ensures the bash configuration is loaded,
# enabling Conda.

conda activate cal_service

# Enable strict mode:
set -euo pipefail

# update cal data
python3 /app/update_cal_data.py

# exec the final command:
exec gunicorn --bind 0.0.0.0:8000 app:app