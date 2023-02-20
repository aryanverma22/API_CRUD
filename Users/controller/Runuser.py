import json
import datetime
import os

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, ForeignKey

from Users.service.services import create,update_user,delete,read
def run():
    app = Flask(__name__)
    # configuration
    app.config['SECRET_KEY'] = 'secretkey'
    secret_key = app.config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/intern"
    return app
    # engine= create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/intern")
app=run()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# print(db.Model)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__='Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email_id = db.Column(db.String(70), unique=True)
    created_by = db.Column(db.String, default=os.getlogin())
    created_at= db.Column(db.Time, default=datetime.datetime.now())
    updated_at= db.Column(db.Time)
    updated_by= db.Column(db.String)

    def __repr__(self):

        # output= "{'ID': ,'Name': {self.name},'email': {self.email_id}}"
        # return output
        return f" ('ID: {self.id}', 'name: {self.name}', 'email_id: {self.email_id}')"



@app.route('/', methods=['GET'])
def read1():
    return read(db,User)

@app.route('/', methods=['Post'])
def create1():
    return create(db,User)

@app.route('/', methods=['Put'])
def update():
    return update_user(db,User)


@app.route('/', methods=['Delete'])
def delete1():
    return delete(db,User)


if __name__ == '__main__':
    app.run(port=3600,debug=True)