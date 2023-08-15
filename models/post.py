from typing import Optional, Type
from pydantic import BaseModel
from pydantic.main import create_model


class Post(BaseModel):
    id: Optional[str]
    title: str
    description: str
    image: str


class PostToSave(BaseModel):
    title: str
    description: str
    image: str


class BaseResponse(BaseModel):
    status: str


class TimeStampedResponse(BaseResponse):
    timeStamp: float


class PostsResponse(TimeStampedResponse):
    data: list[Post]


class PostResponse(TimeStampedResponse):
    data: Post


def create_simple_response_model(name: str, data_model: Type[BaseModel]) -> Type[BaseModel]:
    return create_model(name, data=(data_model, ...), __base__=BaseResponse)


ActionResponse = create_simple_response_model('ActionResponse', Post)
