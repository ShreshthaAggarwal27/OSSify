from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.db.postgres import Base

class Contributor(Base):
    __tablename__ = "contributors"

    id = Column(Integer, primary_key=True, index=True)
    github_id = Column(Integer)
    username = Column(String)
    profile_url = Column(String)
    avatar_url = Column(String)
    contributions_count = Column(Integer)
    repo_id = Column(Integer, ForeignKey("repositories.id"))