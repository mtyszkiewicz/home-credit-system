from collections import defaultdict
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://192.168.1.17",
    "http://192.168.1.17:5173",
    "http://10.0.0.1",
    "http://10.0.0.1:5173"
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


@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No users found")
    return sorted([user.to_dict() for user in users], key=lambda user: user["score"], reverse=True)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()


@app.get(
    "/users/{user_id}/activity_records", response_model=List[schemas.ActivityRecord]
)
def read_user_activity_records(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sorted(user.activity_records, key=lambda record: record.timestamp, reverse=True)


@app.post("/users/{user_id}/activity_records", response_model=schemas.ActivityRecord)
def create_activity_record_for_user(
    user_id: str, activity_id: int, db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    activity = crud.get_activity_by_id(db, activity_id == activity_id)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity_record = crud.create_user_activity_record(
        db=db, user_id=user_id, activity_id=activity_id
    )
    if activity_record is None:
        raise HTTPException(status_code=500, detail="Could not create activity record")
    return activity_record


@app.get("/users/{user_id}/activity_summary", response_model=schemas.UserActivitySummary)
def read_user_activity_summary(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_activity_summary = crud.get_activity_summary_for_user(db, user_id)
    return {
        "user": user.to_dict(),
        "activity_summary": sorted([
            {
                "id": activity.id,
                "name": activity.name,
                "count": count,
                "total_value": total_value,
                "icon": activity.icon,
                "description": activity.description,
                "group_name": activity.group_name,
            }
            for activity, count, total_value in user_activity_summary
        ], lambda activity: activity["total_value"], reverse=True),
    }


@app.get("/activities", response_model=List[schemas.Activity])
def read_activities(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    if len(activities) == 0:
        raise HTTPException(status_code=404, detail="No activities found")
    return sorted(activities, key=lambda activity: activity.name)


@app.get("/activity_records", response_model=List[schemas.ActivityRecordsHistory])
def read_activities_records(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    records = crud.get_activity_records(db, skip=skip, limit=limit)
    if len(records) == 0:
        raise HTTPException(status_code=404, detail="No activity records found")
    records_daily = defaultdict(list)
    for record in records:
        records_daily[record.timestamp.date()].append(record.to_dict())

    return sorted([
        {
            "date": date_str,
            "records": sorted(data, key=lambda record: record["timestamp"], reverse=True)
        }
        for date_str, data in records_daily.items()
    ], key=lambda day: day["date"], reverse=True)


@app.get("/activity_summary", response_model=List[schemas.UserActivitySummary])
def read_activities_summary(db: Session = Depends(get_db)):
    activity_summary = crud.get_activity_summary(db)

    summary_dict = {}
    for user, activity, count, total_value in activity_summary:
        if user.id not in summary_dict:
            summary_dict[user.id] = {"user": user.to_dict(), "activity_summary": []}

        summary_dict[user.id]["activity_summary"].append(
            {
                "id": activity.id,
                "name": activity.name,
                "count": count,
                "total_value": total_value,
                "icon": activity.icon,
                "description": activity.description,
                "group_name": activity.group_name,
            }
        )

    for user_id, data in summary_dict.items():
        summary_dict[user_id]["activity_summary"] = sorted(data["activity_summary"], key=lambda activity: activity["total_value"], reverse=True)
    
    return sorted(list(summary_dict.values()), key=lambda data: data["user"]["score"], reverse=True)
