import re

from typing import AnyStr, List, Union, Dict, TypedDict, Literal
from typing_extensions import Annotated
from pydantic import BaseModel, validator, root_validator, Field


# Auth
class AuthRequest(BaseModel):
    username: str
    password: str

class Storage:
    id: str
    type: str

class S3Storage(Storage):
    type: str = "s3"
    access_key: str
    access_secret: str
    endpoint: str
    bucket: str
    role: str

class Registry:
    id: str
    type: str = "dockerhub"
    storage: S3Storage
    role: str

class PreparedRequest:
    def __init__(
        self,
        is_valid=True,
        body=None,
        message=None,
        failure_view=None
    ):
        self.is_valid = is_valid
        self.body = body
        self.message = message
        self.failure_view = failure_view



