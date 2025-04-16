from sqlalchemy import Column, Integer, String
from data.database import Base  
from data.database import get_session

# Create the session here
SessionLocal = get_session()


class TopGainer(Base):
    __tablename__ = "top_gainers"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    price = Column(String)
    change = Column(String)
    percent_change = Column(String)


class TopLoser(Base):
    __tablename__ = "top_losers"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    price = Column(String)
    change = Column(String)
    percent_change = Column(String)
