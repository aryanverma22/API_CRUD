from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Users.Model.model import User
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

migrate = Migrate(app, db)

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