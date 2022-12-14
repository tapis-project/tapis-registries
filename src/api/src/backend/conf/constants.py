import os

SECRETS_TENANT = "admin"

REGISTRIES_SERVICE_ACCOUNT = os.environ["REGISTRIES_SERVICE_ACCOUNT"]
REGISTRIES_SERVICE_PASSWORD = os.environ["REGISTRIES_SERVICE_PASSWORD"]

TAPIS_DEV_URL = os.environ["TAPIS_DEV_URL"]
TAPIS_DEV_TENANT = "dev" # TODO add to environment variables
LOCAL_DEV_HOSTS = ["127.0.0.1", "localhost", "c006.rodeo.tacc.utexas.edu"]

TAPIS_SERVICE_SITE_ID = os.environ["TAPIS_SERVICE_SITE_ID"]
TAPIS_SERVICE_TENANT_ID = os.environ["TAPIS_SERVICE_TENANT_ID"]
TAPIS_SERVICE_ACCOUNT = REGISTRIES_SERVICE_ACCOUNT
TAPIS_SERVICE_ACCOUNT_PASSWORD = REGISTRIES_SERVICE_PASSWORD
REGISTRIES_SERVICE_URL = os.environ["REGISTRIES_SERVICE_URL"]
TAPIS_SERVICE_LOG_FILE = "/src/logs/registries.logs"

LOG_LEVEL = os.environ["LOG_LEVEL"]

TAPIS_TOKEN_HEADER = "X-TAPIS-TOKEN"

DJANGO_TAPIS_TOKEN_HEADER = f"HTTP_{TAPIS_TOKEN_HEADER.replace('-', '_')}"

PERMITTED_HTTP_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

PERMITTED_CONTENT_TYPES = ["application/json"]