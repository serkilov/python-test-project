from datetime import datetime
from typing import Any, List, Union
from pydantic import BaseModel, AnyHttpUrl


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: Union[str, None]
    address_2: Union[str, None]
    address_3: Union[str, None]
    city: str
    state: Union[str, None]
    county_province: Union[str, None]
    postal_code: str
    country: str
    longitude: Union[float, None]
    latitude: Union[float, None]
    phone: Union[int, None]
    website_url: Union[AnyHttpUrl, None]
    updated_at: datetime
    created_at: datetime


class Breweries(BaseModel):
    __root__: List[Brewery]
