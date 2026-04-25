from typing import Annotated, Optional, Literal
from pydantic.json_schema import SkipJsonSchema
from sqlmodel import Field, SQLModel
from enum import Enum
from decimal import Decimal
import datetime
from datetime import date


class BaseSQLModel(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class Dealer(BaseSQLModel):
    user_id: int = Field(default=None, foreign_key="user.id")
    dealer_pic: str = Field(max_length=256, nullable=False, default="")
    address: str = Field(max_length=128, nullable=False, default="")

class Builder(BaseSQLModel):
    user_id: int = Field(default=None, foreign_key="user.id")
    dealer_pic: str = Field(max_length=256, nullable=False, default="")
    address: str = Field(max_length=128, nullable=False, default="")

class Villa(BaseSQLModel):
    property_id: int = Field(nullable=False, foreign_key="property.id")
    price_per_night: float
    no_of_bedrooms: int
    no_of_bathrooms: int
    has_pool: bool = False
    description: Optional[str] = None

class FarmHouse(BaseSQLModel):
    property_id: int = Field(nullable=False, foreign_key="property.id")
    description: Optional[str] = None
