from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    icon = Column(String, unique=True)
    value = Column(Integer)
    description = Column(String)
    group_name = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)

    @property
    def score(self):
        return sum([record.activity.value for record in self.activity_records])

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "score": self.score,
        }


class ActivityRecord(Base):
    __tablename__ = "activity_records"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(TIMESTAMP, server_default=text("(CURRENT_TIMESTAMP)"))

    user = relationship("User", backref="activity_records", foreign_keys=[user_id])
    activity = relationship(
        "Activity", backref="activity_records", foreign_keys=[activity_id]
    )
