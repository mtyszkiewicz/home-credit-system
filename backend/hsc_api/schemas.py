from typing import List
from pydantic import BaseModel, Field
import datetime


class User(BaseModel):
    id: str = Field(..., description="Unique ID of the user")
    name: str = Field(..., description="Name of the user")
    image: str = Field(..., description="Static image filename representing the user's profile")
    score: int = Field(..., description="Aggregate score of the user based on activity values")
    color: str = Field(...)

    class Config:
        orm_mode = True


class Activity(BaseModel):
    id: int
    name: str = Field(..., description="Name of the activity")
    value: int = Field(..., description="Score value associated with the activity")
    icon: str = Field(..., description="Icon emoji representing the activity")

    class Config:
        orm_mode = True


class ActivityRecord(BaseModel):
    id: int = Field(..., description="Unique ID of the activity record")
    timestamp: datetime.datetime = Field(..., description="Time when the activity record was created")
    user: User = Field(..., description="The user associated with the activity record")
    activity: Activity = Field(..., description="The activity associated with the record")
    time: str

    class Config:
        orm_mode = True

class ActivityRecordsHistory(BaseModel):
    date: datetime.date
    records: List[ActivityRecord]

    class Config:
        orm_mode = True


class ActivityRecordCreate(BaseModel):
    user_id: int = Field(..., description="ID of the user for whom the activity record is being created")
    activity_id: int = Field(..., description="ID of the activity for the activity record")


class ActivitySummary(BaseModel):
    id: int = Field(..., description="ID of the activity in the summary")
    name: str = Field(..., description="Name of the activity in the summary")
    count: int = Field(..., description="Count of this activity performed by the user")
    total_value: int = Field(..., description="Total value earned by the user through this activity")
    icon: str = Field(..., description="Icon emoji representing the activity")
    description: str = Field(..., description="Description of the activity")

    class Config:
        orm_mode = True


class UserActivitySummary(BaseModel):
    user: User = Field(..., description="The user for whom the activity summary is being reported")
    activity_summary: List[ActivitySummary] = Field(..., description="List of summaries of activities performed by the user")

    class Config:
        orm_mode = True
