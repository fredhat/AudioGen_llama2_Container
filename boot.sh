#!/bin/sh
exec gunicorn -k uvicorn.workers.UvicornWorker -b :5000 --timeout 1800 api:app