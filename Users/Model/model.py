import datetime
import os
from sqlalchemy import Column, Integer, String, Time
from Repo.Connection import Base

# Base= declarative_base()

class User(Base):
    __tablename__='Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(50), unique=True)
    name = Column(String(100))
    email_id = Column(String(70), unique=True)
    created_by = Column(String, default=os.getlogin())
    created_at= Column(Time, default=datetime.datetime.now())
    updated_at= Column(Time)
    updated_by= Column(String)

    def __repr__(self):

        # output= "{'ID': ,'Name': {self.name},'email': {self.email_id}}"
        # return output
        return f" ('ID: {self.id}', 'name: {self.name}', 'email_id: {self.email_id}')"
