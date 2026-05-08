from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.db.postgres import Base

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)
    issue_number = Column(Integer)
    title = Column(String)
    body = Column(String)
    state = Column(String)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    repo_id = Column(Integer, ForeignKey("repositories.id"))
    repository = relationship("Repository", back_populates="issues")