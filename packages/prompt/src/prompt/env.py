from pydantic import BaseModel
from pydantic.types import StringConstraints
from typing import Annotated

from dotenv import load_dotenv
import os

load_dotenv()

NonEmptyString = Annotated[str, StringConstraints(min_length=1)]

class Env(BaseModel):
    AZURE_OPENAI_ENDPOINT: NonEmptyString
    AZURE_OPENAI_KEY: NonEmptyString
    AZURE_SEARCH_ENDPOINT: NonEmptyString
    AZURE_SEARCH_KEY: NonEmptyString
    AZURE_OPENAI_DEPLOYMENT_NAME: NonEmptyString
    AZURE_OPENAI_EMBEDDING_NAME: NonEmptyString

env = Env(
    AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT"),
    AZURE_OPENAI_KEY=os.getenv("AZURE_OPENAI_KEY"),
    AZURE_SEARCH_ENDPOINT=os.getenv("AZURE_SEARCH_ENDPOINT"),
    AZURE_SEARCH_KEY=os.getenv("AZURE_SEARCH_KEY"),
    AZURE_OPENAI_DEPLOYMENT_NAME=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    AZURE_OPENAI_EMBEDDING_NAME=os.getenv("AZURE_OPENAI_EMBEDDING_NAME"),
)