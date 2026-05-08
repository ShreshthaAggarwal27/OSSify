from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.db.postgres import Base

class Contributor(Base):
    __tablename__ = "contributors"

    id = Column(Integer, primary_key=True, index=True)
    github_id = Column(Integer, unique=True, nullable=False, index=True)
    username = Column(String, nullable=False, index=True)
    profile_url = Column(String)
    avatar_url = Column(String)
    contributions_count = Column(Integer)
    commits = relationship("Commit", back_populates="contributor")
