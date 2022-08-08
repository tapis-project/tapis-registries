#!/bin/bash

chmod a+x ./scripts/init.sh
./scripts/init.sh
gunicorn --bind 0.0.0.0:8000 --workers 2 registries.wsgi --worker-class gevent --timeout 600