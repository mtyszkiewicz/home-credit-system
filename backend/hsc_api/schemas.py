# from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    name: str
    group_name: str


# class Activity(ActivityBase):
#     id: int

#     class Config:
#         orm_mode = True