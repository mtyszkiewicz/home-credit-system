from collections import defaultdict
from typing import List
import uuid

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://192.168.1.17",
    "http://192.168.1.17:5173",
    "http://10.0.0.1",
    "http://10.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/auth", response_model=schemas.User)
def authorize(access_token: uuid.UUID, db: Session = Depends(get_db)):
    user = crud.get_user_by_access_token(db, access_token=access_token)
    if user is None:
        raise HTTPException(status_code=404, detail="Unauthorized")
    return user.to_dict()


@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@app.get("/activities", response_model=List[schemas.Activities])
def read_activities(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    if len(activities) == 0:
        raise HTTPException(status_code=404, detail="No activities found")
    return sorted(activities, key=lambda activity: activity.name)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()


@app.post(
    "/users/{user_id}/activity_records", response_model=schemas.ActivityRecordsCreate
)
def create_activity_record_for_user(
    user_id: str, activity_id: int, db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    activity = crud.get_activity_by_id(db, activity_id=activity_id)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    new_activity_record = crud.create_new_activity_record(
        db=db, user_id=user_id, activity_icon=activity.icon
    )
    if new_activity_record is None:
        raise HTTPException(status_code=500, detail="Could not create activity record")
    return new_activity_record.__dict__


@app.get("/activity_records", response_model=List[schemas.ActivityRecordsHistory])
def read_activities_records(db: Session = Depends(get_db)):
    records = crud.get_activity_records_daily(db)
    if len(records) == 0:
        raise HTTPException(status_code=404, detail="No activity records found")

    records_daily = defaultdict(list)
    for record in records:
        records_daily[record.date].append(record.to_dict())

    return [
        {"date": date_str, "records": data} for date_str, data in records_daily.items()
    ]


@app.get("/activity_summary", response_model=List[schemas.UserActivitySummary])
def read_activities_summary(db: Session = Depends(get_db)):
    activity_summary = crud.get_activity_summary(db)
    result = {}

    for item in activity_summary:
        if item.user.id not in result:
            result[item.user.id] = {"user": item.user.to_dict(), "activity_summary": []}

        result[item.user.id]["activity_summary"].append(
            {
                "id": item.activity.id,
                "name": item.activity.name,
                "count": item.activity_total_count,
                "total_value": item.activity_total_value,
                "icon": item.activity.icon,
            }
        )
    return list(result.values())
