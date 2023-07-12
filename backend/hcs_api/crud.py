import uuid
from typing import List

from sqlalchemy.orm import Session

from . import models


def get_users(db: Session) -> List[models.User]:
    """Retrieves all users."""
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: str) -> models.User:
    """Retrieves a user with matching user_id"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_access_token(db: Session, access_token: uuid.UUID) -> models.User:
    """
    Retrieves a user with matching access_token.
    This authorization method will be deprecated in future versions.
    """
    return (
        db.query(models.User).filter(models.User.access_token == access_token).first()
    )


def get_activities(db: Session) -> List[models.Activity]:
    """
    Retrieves all most recently updated activities.
    The full history of activityies is stored in the source table.
    """
    return db.query(models.Activity).all()


def get_activity_by_id(db: Session, activity_id: int) -> models.Activity:
    """Retrieves an activity with matching activity_id."""
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()


def get_activity_summary(db: Session) -> List[models.ActivityRecordSummary]:
    """Retrieves the activities summary (counts and value sum)."""
    return db.query(models.ActivityRecordSummary).all()


def get_activity_records_daily(db: Session) -> List[models.ActivityRecordDaily]:
    """Retrieves the history of all activites."""
    return db.query(models.ActivityRecordDaily).all()


def create_new_activity_record(
    db: Session, user_id: int, activity_icon: str
) -> models.SourceActivityRecord:
    """Creates a new activity record in the source table; marks the activity as done by the user."""
    activity_record = models.SourceActivityRecord(
        activity_icon=activity_icon, user_id=user_id
    )
    db.add(activity_record)
    db.commit()
    db.refresh(activity_record)
    return activity_record
