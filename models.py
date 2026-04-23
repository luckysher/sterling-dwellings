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

