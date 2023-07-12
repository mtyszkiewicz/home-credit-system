from sqlalchemy import Column, ForeignKey, Integer, String, text, DateTime, UUID, DATE
from sqlalchemy.orm import relationship

from .database import Base


class SourceActivity(Base):
    """
    Activities source table.

    This table tracks history (SCD2) of all activites and how they were updated in time.
    Latest activities are available in Activity class, which represents a view with necessary transformations.
    All inserts to this source table are done only by the ingestion scripts.
    """

    __tablename__ = "activities"
    __table_args__ = {"schema": "raw"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    icon = Column(String, unique=True)
    value = Column(Integer)
    start_date = Column(DATE)
    end_date = Column(DATE)


class SourceUser(Base):
    """
    Users source table.
    All inserts to this table are done only by the ingestion scripts.
    """

    __tablename__ = "users"
    __table_args__ = {"schema": "raw"}

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(UUID)
    name = Column(String)
    image = Column(String)
    color = Column(String)


class SourceActivityRecord(Base):
    """
    Activity Records source table.
    Here the new done activities get inserted.
    """

    __tablename__ = "activity_records"
    __table_args__ = {"schema": "raw"}

    id = Column(Integer, primary_key=True, index=True)
    activity_icon = Column(String)
    user_id = Column(Integer, ForeignKey("raw.users.id"))
    create_timestamp = Column(DateTime, server_default=text("(CURRENT_TIMESTAMP)"))

    user = relationship(
        "SourceUser", backref="activity_records", foreign_keys=[user_id]
    )


class Activity(Base):
    __tablename__ = "activities"
    __table_args__ = {"schema": "dwh"}

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    icon = Column(String, unique=True)
    value = Column(Integer)


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "dwh"}

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
            "score": self.score,
        }


class ActivityRecordSummary(Base):
    __tablename__ = "activity_records_summary"
    __table_args__ = {"schema": "dwh"}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("dwh.users.id"))
    activity_id = Column(Integer, ForeignKey("raw.activities.id"))
    activity_total_value = Column(Integer)
    activity_total_count = Column(Integer)
    user_total_score = Column(Integer)

    user = relationship("User", foreign_keys=[user_id])
    activity = relationship("SourceActivity", foreign_keys=[activity_id])


class ActivityRecordDaily(Base):
    __tablename__ = "activity_records_daily"
    __table_args__ = {"schema": "dwh"}

    id = Column(Integer, primary_key=True)
    date = Column(DATE)
    time = Column(String)
    user_id = Column(Integer, ForeignKey("dwh.users.id"))
    activity_id = Column(Integer, ForeignKey("raw.activities.id"))

    user = relationship("User", foreign_keys=[user_id])
    activity = relationship("SourceActivity", foreign_keys=[activity_id])

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "time": self.time,
            "user": self.user.to_dict(),
            "activity": self.activity,
        }
