import datetime
import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, Sequence, String, Time
from Users.Model.model import User
from Repo.Connection import Base

class Post(Base):
    __tablename__='posts'
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id))
    caption = Column(String(100))
    location= Column(String)
    created_by = Column(String, default=os.getlogin())
    created_at= Column(Time, default=datetime.datetime.now())
    updated_at= Column(Time)
    updated_by= Column(String)
