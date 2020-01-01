#!/usr/bin/env bash
export PYTHONPATH=src/
gunicorn app:app -b 0.0.0.0:8000 --worker-class aiohttp.GunicornWebWorker --access-logfile -
