# from typing import Union

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str
    name: str
    image: str = Field(description="Static image filename.")

    class Config:
        orm_mode = True

class Activity(BaseModel):
    # id: int
    name: str
    score: int
    icon: str = Field(description="Icon emoji")
    # description: str
    group_name: str

    class Config:
        orm_mode = True

class ActivityLog(BaseModel):
    id: int
    timestamp: str = Field(None)
    user: User
    activity: Activity

    class Config:
        orm_mode = True