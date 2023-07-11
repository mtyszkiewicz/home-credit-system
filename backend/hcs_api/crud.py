from typing import List
import uuid

from sqlalchemy.orm import Session

from . import models


def get_users(db: Session) -> List[models.User]:
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: str) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def is_valid_uuid(val: str) -> bool:
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def get_user_by_access_token(db: Session, access_token: str) -> models.User:
    if not is_valid_uuid(access_token):
        return None
    return (
        db.query(models.User)
        .filter(models.User.access_token == access_token)
        .first()
    )


def create_user_activity_record(
    db: Session, user_id: int, activity_icon: str
) -> models.SourceActivityRecord:
    activity_record = models.SourceActivityRecord(activity_icon=activity_icon, user_id=user_id)
    db.add(activity_record)
    db.commit()
    db.refresh(activity_record)
    return activity_record


def get_activity_summary_for_user(db: Session, user_id: int):
    return (
        db.query(models.ActivityRecordSummary)
        .filter(models.ActivityRecordSummary.user_id == user_id)
        .all()
    )


def get_activity_summary(db: Session):
    return db.query(models.ActivityRecordSummary).all()


def get_activities(db: Session) -> List[models.Activity]:
    """Retrieves all home activities possible."""
    return db.query(models.Activity).all()


def get_activity_by_id(db: Session, activity_id: int) -> models.Activity:
    """Retrieves a specific home activity by it's ID."""
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()


def get_activity_records_daily(
    db: Session, skip: int = 0, limit: int = 100
) -> List[models.ActivityRecordDaily]:
    """Retrieves full history of activites for all users."""
    return db.query(models.ActivityRecordDaily).offset(skip).limit(limit).all()
