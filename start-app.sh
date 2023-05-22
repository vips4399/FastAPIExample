#!/bin/bash

# Define the path to the gunicorn_config.py file
CONFIG_FILE="gunicorn_config.py"

# Run gunicorn with the specified configuration file and module
gunicorn -c "$CONFIG_FILE" src.main:app