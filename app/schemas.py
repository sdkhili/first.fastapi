from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

from app.routers import post

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  #default true

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        #orm_mode = True
        from_attributes = True


class PostRespond(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        #orm_mode = True
        from_attributes = True

class PostOut(BaseModel):
    Post: PostRespond
    votes: int

    class Config:
        #orm_mode = True
        from_attributes = True
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore


