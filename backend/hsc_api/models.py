from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship

from .database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    score = Column(Integer)
    description = Column(String)
    group_name = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)

    @property
    def score(self):
        return sum([log.activity.score for log in self.activity_logs])

class ActivityLog(Base):
    __tablename__ = "activities_log"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(TIMESTAMP, default=func.now())

    user = relationship("User", backref="activity_logs", foreign_keys=[user_id])
    activity = relationship("Activity", backref="activity_logs", foreign_keys=[activity_id])
