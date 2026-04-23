from typing import Annotated, Optional, Literal
from pydantic.json_schema import SkipJsonSchema
from sqlmodel import Field, SQLModel
from enum import Enum
import datetime

class PropertyTypeBase(str, Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"

class PropertyTypeExtended(str, Enum):
    FLAT = "flat"
    RESIDENTIAL_LAND = "residential_land"
    SERVICE_APARTMENT = "service_apartment"
    STUDIO_APARTMENT = "studio_apartment"
    FARM_HOUSE = "farm_house"
    BUILDER_FLOOR = "builder_floor"
    VILLA = "villa"
    OTHER = "other"

class User(SQLBaseModel):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(max_length=64, nullable=False)
    email: str = Field(unique=True, max_length=64, nullable=False)
    password: Optional[str]
    contact_no: str = Field(nullable=False, default="")
    active: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    is_admin: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    last_login: Annotated[datetime.datetime | None, SkipJsonSchema()] = Field(default=None)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class Dealer(SQLBaseModel):
    user_id: int = Field(default=None, foreign_key="user.id")
    dealer_pic: str = Field(max_length=256, nullable=False, default="")
    name: str = Field(max_length=64, nullable=False)
    address: str = Field(max_length=128, nullable=False, default="")

