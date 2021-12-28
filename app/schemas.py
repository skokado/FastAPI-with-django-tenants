from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    author_id: int
    title: str
    body: str


class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True
