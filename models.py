from typing import Annotated, Optional, Literal
from pydantic.json_schema import SkipJsonSchema
from sqlmodel import Field, SQLModel
from enum import Enum
import datetime


class BaseSQLModel(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())
