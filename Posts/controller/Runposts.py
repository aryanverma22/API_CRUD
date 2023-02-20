from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Posts.Model.model import User,Post
from Posts.service.services import create,update_post,delete,read

def run():
    app = Flask(__name__)
    # configuration
    app.config['SECRET_KEY'] = 'secretkey'
    secret_key = app.config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/intern"
    return app
app=run()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# print(db.Model)
migrate = Migrate(app, db)


@app.route('/', methods=['GET'])
def read1():
    return read(db,Post)

@app.route('/', methods=['Post'])
def create1():
    return create(db,Post,User)

@app.route('/', methods=['Put'])
def update():
    return update_post(db,Post)


@app.route('/', methods=['Delete'])
def delete1():
    return delete(db,Post)

