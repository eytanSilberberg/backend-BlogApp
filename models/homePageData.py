from typing import Optional
from pydantic import BaseModel


class HomePageData(BaseModel):
    heading: str
    paragraph: str


class HomePageDataResponse(BaseModel):
    data: HomePageData
    status: str
