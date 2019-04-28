#/!bin/bash

source venv/bin/activate
echo activated
gunicorn --config gunicorn_config main:app
