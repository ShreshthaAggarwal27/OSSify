from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.app.db.postgres import Base

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    full_name = Column(String, unique=True, nullable=False, index=True)
    url = Column(String, nullable=False)
    commits = relationship("Commit", back_populates="repository")
    pull_requests = relationship("PullRequest", back_populates="repository")
    issues = relationship("Issue", back_populates="repository")