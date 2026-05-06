from sqlalchemy import Column, Integer, String
from backend.app.db.postgres import Base

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(String)
    full_name = Column(String)
    url = Column(String)