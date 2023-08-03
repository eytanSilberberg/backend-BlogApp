from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    image: str


class PostToSave(BaseModel):
    title: str
    description: str
    image: str


class PostsResponse(BaseModel):
    data: list[Post]
    status: str
    timeStamp: float


class PostResponse(BaseModel):
    data: Post
    status: str
    timeStamp: float


class PostToSaveResponse(BaseModel):
    data: Post
    status: str


class PostToUpdateResponse(BaseModel):
    data: Post
    status: str


class PostToDeleteResponse(BaseModel):
    data: Post
    status: str
