from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException

from . import models, schemas


def get_activities(db: Session) -> List[schemas.Activity]:
    return db.query(models.Activity).all()


def get_users(db: Session) -> List[schemas.User]:
    return db.query(models.User).all()

def get_user_by_id(db: Session, user_id: str) -> schemas.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_activities_log(
    db: Session, skip: int = 0, limit: int = 100
) -> List[schemas.ActivityLog]:
    return db.query(models.ActivityLog).offset(skip).limit(limit).all()


def get_user_total_score(db: Session):
    return (
        db.query(
            models.User,
            func.sum(models.Activity.score).label("total_score"),
        )
        .join(models.ActivityLog, models.ActivityLog.user_id == models.User.id)
        .join(models.Activity, models.ActivityLog.activity_id == models.Activity.id)
        .group_by(models.User.id)
        .all()
    )


def get_user_activity_counts(db: Session):
    return (
        db.query(
            models.User,
            models.Activity,
            func.count(models.ActivityLog.id).label("activity_count"),
        )
        .join(models.ActivityLog, models.ActivityLog.user_id == models.User.id)
        .join(models.Activity, models.ActivityLog.activity_id == models.Activity.id)
        .group_by(models.User.id, models.Activity.id)
        .all()
    )


def create_user_activities_log(db: Session, user_id: int, activity_id: int) -> schemas.ActivityLog:
    activity = (
        db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    )
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    activity_log = models.ActivityLog(activity_id=activity.id, user_id=user.id)
    db.add(activity_log)
    db.commit()
    db.refresh(activity_log)
    return activity_log


def delete_activity_log(db: Session, id: int) -> schemas.ActivityLog:
    activity_log = (
        db.query(models.ActivityLog).filter(models.ActivityLog.id == id).first()
    )
    if activity_log is None:
        raise HTTPException(status_code=404, detail="Activity log not found")
    db.delete(activity_log)
    db.commit()
    return activity_log
