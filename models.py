from typing import Annotated, Optional, Literal
from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from enum import Enum
from decimal import Decimal
import datetime
from datetime import date

class UserLoginCredential(BaseModel):

    email: str
    password: str

# user model
class User(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(index=True, max_length=64, nullable=False)
    email: str = Field(unique=True, max_length=64, nullable=False)
    password: str = Field(nullable=False)
    is_dealer: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    is_admin: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    last_login: Annotated[datetime.datetime | None, SkipJsonSchema()] = Field(default=None)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

# dealer user model
class Dealer(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    dealer_pic: str = Field(max_length=256, default="")
    address: str = Field(max_length=128, nullable=False, default="")
    approved: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class Builder(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    dealer_pic: str = Field(max_length=256, nullable=False, default="")
    address: str = Field(max_length=128, nullable=False, default="")
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class Villa(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    property_id: int = Field(nullable=False, foreign_key="property.id")
    price_per_night: float
    no_of_bedrooms: int
    no_of_bathrooms: int
    has_pool: bool = False
    description: Optional[str] = None
    sqft: int
    price: float = Field(index=True)
    has_garden: bool = Field(default=False)
    is_available: bool = Field(default=True)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class FarmHouse(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    property_id: int = Field(nullable=False, foreign_key="property.id")
    description: Optional[str] = None
    acreage: float
    has_pool: bool = False
    price_per_night: float
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())


class DealerInput(BaseModel):
    name: str
    email: str
    password: str
    dealer_pic: str
    address: str
