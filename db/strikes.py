from db.base import Base
from sqlalchemy import Column, Integer, Date, String, DateTime, func


class Strikes(Base):

    __tablename__ = "strike_info"

    id = Column(Integer, primary_key=True)
    date_of_strike = Column(Date)
    strike_message = Column(String)
    date_added_to_db = Column(DateTime(timezone=True), server_default=func.now())
