from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, text, DateTime, ARRAY
from sqlalchemy.orm import relationship

from .database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    icon = Column(String, unique=True)
    value = Column(Integer)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    color = Column(String)

    @property
    def score(self):
        return sum([record.activity.value for record in self.activity_records])

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "score": self.score,
            "color": self.color
        }


class ActivityRecord(Base):
    __tablename__ = "activity_records"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, server_default=text("(CURRENT_TIMESTAMP)"))

    user = relationship("User", backref="activity_records", foreign_keys=[user_id])
    activity = relationship(
        "Activity", backref="activity_records", foreign_keys=[activity_id]
    )

    @property
    def date(self):
        return self.timestamp.date()
    
    @property
    def time(self):
        return str(self.timestamp.time())[:5]

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "time": self.time,
            "user": self.user,
            "activity": self.activity,
        }
