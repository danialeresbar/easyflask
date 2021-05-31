#!/bin/sh

exec "$@"

python manage.py run -h 0.0.0.0
