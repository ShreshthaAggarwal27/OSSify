from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app.db.postgres import Base

class Commit(Base):
    __tablename__ = "commits"

    id = Column(Integer, primary_key=True)
    sha = Column(String, unique=True)
    message = Column(String)
    author_name = Column(String)
    author_email = Column(String)
    date = Column(DateTime)
    repo_id = Column(Integer, ForeignKey("repositories.id"))