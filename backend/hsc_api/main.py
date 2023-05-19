from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/activities", response_model=List[schemas.Activity])
def read_activities(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    return activities


@app.get("/activities_log", response_model=List[schemas.ActivityLog])
def read_activities_log(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = crud.get_activities_log(db, skip=skip, limit=limit)
    return [{"id": log.id, "user": log.user, "activity": log.activity} for log in logs]


@app.get("/summary")
def read_user_summary(db: Session = Depends(get_db), user_id: str = None):
    total_scores = crud.get_user_total_score(db)
    activity_counts = crud.get_user_activity_counts(db)

    result = [
        {
            "user": user,
            "total_score": total_score,
            "activities": [
                {
                    "name": activity.name,
                    "icon": activity.icon,
                    "count": count,
                    "score": count * activity.score
                }
                for _user, activity, count in activity_counts
                if _user.id == user.id
            ]
        }
        for user, total_score in total_scores
    ]
    if user_id is not None:
        return [user for user in result if user["user"].id == user_id][0]

    return result


@app.get("/total_scores")
def read_user_total_score(db: Session = Depends(get_db)):
    total_scores = crud.get_user_total_score(db)
    return [
        {"user_id": user.id, "user_name": user.name, "total_score": total_score}
        for user, total_score in total_scores
    ]


@app.get("/activity_counts")
def read_user_activity_counts(db: Session = Depends(get_db)):
    activity_counts = crud.get_user_activity_counts(db)
    return [
        {
            "user_id": user.id,
            "user_name": user.name,
            "activity_name": activity.name,
            "activity_count": count,
        }
        for user, activity, count in activity_counts
    ]


@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.get("/users/{user_id}")
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=user_id)
    return user


@app.post("/activities_log")
def create_user_activities_log(
    user_id: str, activity_id: int, db: Session = Depends(get_db)
):
    activity_log = crud.create_user_activities_log(
        db, user_id=user_id, activity_id=activity_id
    )
    return activity_log

@app.delete("/activity_log/{id}")
def delete_activity_log(id: int, db: Session = Depends(get_db)):
    crud.delete_activity_log(db, id)
    return {"message": "Activity log deleted"}
