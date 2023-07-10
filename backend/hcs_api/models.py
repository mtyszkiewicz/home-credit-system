from sqlalchemy import Column, ForeignKey, Integer, String, text, DateTime, UUID, DATE
from sqlalchemy.orm import relationship

from .database import Base


class Activities(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    icon = Column(String, unique=True)
    value = Column(Integer)

class ActivitiesLatest(Base):
    __tablename__ = "latest_activities"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    icon = Column(String, unique=True)
    value = Column(Integer)


class User(Base):
    __tablename__ = "users_new"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(UUID)
    name = Column(String)
    image = Column(String)
    color = Column(String)
    
class UserProfile(Base):
    __tablename__ = "users_profile"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(UUID)
    name = Column(String)
    image = Column(String)
    color = Column(String)
    score = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "color": self.color,
            "score": self.score
        }



class ActivityRecords(Base):
    __tablename__ = "activity_records_new"

    id = Column(Integer, primary_key=True, index=True)
    activity_icon = Column(String)
    user_id = Column(Integer, ForeignKey("users_new.id"))
    create_timestamp = Column(DateTime, server_default=text("(CURRENT_TIMESTAMP)"))

    user = relationship("User", backref="activity_records_new", foreign_keys=[user_id])


class ActivityRecordsSummary(Base):
    __tablename__ = "activity_records_summary"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users_profile.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    activity_total_value = Column(Integer)
    activity_total_count = Column(Integer)
    user_total_score = Column(Integer)

    user = relationship("UserProfile", foreign_keys=[user_id])
    activity = relationship(
        "Activities", foreign_keys=[activity_id]
    )

class ActivityRecordsDaily(Base):
    __tablename__ = "activity_records_daily"

    id = Column(Integer, primary_key=True)
    date = Column(DATE)
    time = Column(String)
    user_id = Column(Integer, ForeignKey("users_profile.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))

    user = relationship("UserProfile", foreign_keys=[user_id])
    activity = relationship(
        "Activities", foreign_keys=[activity_id]
    )

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "time": self.time,
            "user": self.user.to_dict(),
            "activity": self.activity,
        }