from sqlalchemy.sql.expression import null
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from .database import Base
from sqlalchemy.orm import Relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable= False)
    published = Column(Boolean, server_default='TRUE', nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = Relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, nullable= False)
    email = Column(String, nullable= False, unique=True)
    password = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    phone_number = Column(String)

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True, nullable=False)
    

