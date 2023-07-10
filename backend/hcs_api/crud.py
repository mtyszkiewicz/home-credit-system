from typing import List
import uuid

from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models


def get_users(db: Session) -> List[models.User]:
    return db.query(models.UserProfile).all()


def get_user_by_id(db: Session, user_id: str) -> models.User:
    return db.query(models.UserProfile).filter(models.UserProfile.id == user_id).first()

def is_valid_uuid(val: str) -> bool:
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def get_user_by_access_token(db: Session, access_token: str) -> models.User:
    if not is_valid_uuid(access_token):
        return None
    return db.query(models.UserProfile).filter(models.UserProfile.access_token == access_token).first()


def create_user_activity_record(
    db: Session, user_id: int, activity_id: int
) -> models.ActivityRecords:
    activity_record = models.ActivityRecords(activity_id=activity_id, user_id=user_id)
    db.add(activity_record)
    db.commit()
    db.refresh(activity_record)
    return activity_record


def get_activity_summary_for_user(db: Session, user_id: int):
    return (
        db.query(
            models.Activities,
            func.count(models.ActivityRecords.id).label("count"),
            func.sum(models.Activities.value).label("total_value"),
        )
        .join(models.ActivityRecords)
        .filter(models.ActivityRecords.user_id == user_id)
        .group_by(models.Activities.id)
        .all()
    )


def get_activity_summary(db: Session):
    return (
        db.query(
            models.User,
            models.Activities,
            func.count(models.ActivityRecords.id).label("count"),
            func.sum(models.Activities.value).label("total_value"),
        )
        .join(models.ActivityRecords, models.User.id == models.ActivityRecords.user_id)
        .join(models.Activities, models.ActivityRecords.activity_id == models.Activities.id)
        .group_by(models.User, models.Activities)
        .all()
    )


def get_activities(db: Session) -> List[models.Activities]:
    """Retrieves all home activities possible."""
    return db.query(models.ActivitiesLatest).all()


def get_activity_by_id(db: Session, activity_id: int) -> models.Activities:
    """Retrieves a specific home activity by it's ID."""
    return db.query(models.Activities).filter(models.Activities == activity_id)


def get_activity_records(
    db: Session, skip: int = 0, limit: int = 100
) -> List[models.ActivityRecords]:
    """Retrieves full history of activites for all users."""
    return db.query(models.ActivityRecords).offset(skip).limit(limit).all()


# def delete_activity_record(db: Session, id: int) -> models.ActivityRecords:
#     activity_log = (
#         db.query(models.ActivityRecords).filter(models.ActivityRecords.id == id).first()
#     )
#     if activity_log is None:
#         raise HTTPException(status_code=404, detail="Activity log not found")
#     db.delete(activity_log)
#     db.commit()
#     return activity_log
