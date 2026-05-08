from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.db.postgres import Base

class PullRequest(Base):
    __tablename__ = "pull_requests"

    id = Column(Integer, primary_key=True)
    pr_number = Column(Integer)
    title = Column(String)
    body = Column(String)
    state = Column(String)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("contributors.id"))
    repo_id = Column(Integer, ForeignKey("repositories.id"))
    repository = relationship("Repository", back_populates="pull_requests")