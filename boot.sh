#!/bin/sh
exec gunicorn -b :5000 --timeout 1800 api:app