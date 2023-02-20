import json
import datetime
import os

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, ForeignKey



app = Flask(__name__)
# configuration
app.config['SECRET_KEY'] = 'secretkey'
secret_key = app.config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/intern"
# engine= create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/intern")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)




# class User(db.Model):
#     __tablename__='Users'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # public_id = db.Column(db.String(50), unique=True)
#     name = db.Column(db.String(100))
#     email_id = db.Column(db.String(70), unique=True)
#     created_by = db.Column(db.String, default=os.getlogin())
#     created_at= db.Column(db.Time, default=datetime.datetime.now())
#     updated_at= db.Column(db.Time)
#     updated_by= db.Column(db.String)
#
#     def __repr__(self):
#
#         # output= "{'ID': ,'Name': {self.name},'email': {self.email_id}}"
#         # return output
#         return f" ('ID: {self.id}', 'name: {self.name}', 'email_id: {self.email_id}')"
#     # db.session.commit()

# class Post(db.Model):
#     __tablename__='posts'
#     post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, ForeignKey(User.id))
#     caption = db.Column(db.String(100))
#     location= db.Column(db.String)
#     created_by = db.Column(db.String, default=os.getlogin())
#     created_at= db.Column(db.Time, default=datetime.datetime.now())
#     updated_at= db.Column(db.Time)
#     updated_by= db.Column(db.String)

# @app.route('/read', methods=['GET'])
# def read():
#
#     # trial= User(name= ' Aryan',id= 4)
#     db.create_all()
#     # db.session.delete()
#     # db.session.add(trial)
#     # User.query.filter_by(id = 4).delete()
#     db.session.commit()
#
#     data = User.query.all()
#
#     out={}
#     print(data[1])
#     i=0
#     for x in data:
#         i+=1
#         temp={'ID': x.id,
#               'Name': x.name,
#               'Email_id': x.email_id}
#         out[f'User {i}']= temp
#
#     return (out)
#
# @app.route('/create', methods=['Post'])
# def new():
#     data= request.form
#     name1= data.get("name")
#     email1= data.get("email")
#
#     present = User.query.filter_by(email_id= email1).first()
#
#     if not present:
#         new = User(name= name1, email_id= email1)
#         db.session.add(new)
#         db.session.commit()
#
#         return make_response("User successfully added",201)
#     else:
#         return make_response("User already present",202)
#
# @app.route('/', methods=['Put'])
# def update_user():
#     data= request.form
#     user_id= data.get("user_id")
#     col_to_change= data.get("change_in")
#     new= data.get("new_data")
#     present = User.query.filter_by(id=user_id).first()
#     if not present:
#         return make_response("User not present",202)
#     else:
#         if col_to_change == "email":
#             present1 = User.query.filter_by(email_id= new).first()
#             if present1:
#                 return make_response("Email already registered", 202)
#             else:
#                 present.email_id= new
#                 present.updated_at= datetime.datetime.now()
#                 present.updated_by= os.getlogin()
#                 db.session.commit()
#                 return make_response("Data updated successfully",201)
#         elif col_to_change == "name":
#             present.name = new
#             present.updated_at = datetime.datetime.now()
#             present.updated_by = os.getlogin()
#             db.session.commit()
#             return make_response("Data updated successfully", 201)
#         else:
#             return make_response("No such Attribute present", 202)
#
# @app.route('/delete', methods=['Delete'])
# def remove():
#     data=request.form
#     uid= data.get("user_id")
#     print(uid)
#     present = User.query.filter_by(id=uid).first()
#     if not present:
#         return make_response("User not present", 202)
#     else:
#         db.session.delete(present)
#         db.session.commit()
#         return make_response("User deleted successfully",201)
#
#
#
#
#
#     # change= data.get("new_name")
#     # # print(id, email)
#     # if email:
#     #     present = User.query.filter_by(email_id=email).first()
#     #     if not present:
#     #         return make_response("User not present",202)
#     #     else:

@app.route('/newpost', methods=['Post'])
def newposts():
    data= request.json
    ps=data['Posts']
    print(ps)
    out={}
    for ele in ps:
        cap=ele['Caption']
        uid=int(ele['User_id'])
        loc=ele['location']
        present = User.query.filter_by(id= uid).first()
        if not present:
            out[uid]= 'User not present'
        else:
            new = Post(user_id=uid, caption =cap, location=loc)
            db.session.add(new)
            db.session.commit()
            out[uid]='Posts added successfully'
    return make_response(out)

    # cap= data.get("caption")
    # userid= data.get("user_id")
    # new = Post(user_id= userid, caption=cap)
    # db.session.add(new)
    # db.session.commit()
    return make_response("jjk")

@app.route('/readposts', methods=['GET'])
def watch():
    data=request.form
    uid=data.get("user_id")
    present = Post.query.filter_by(user_id=uid)
    if not present:
        return make_response("No posts found")

    output={}
    i=0
    for x in present:
        i+=1
        temp={}
        print((x))
        temp={"Post_ID": x.post_id,
              "User_ID": x.user_id,
              "Caption": x.caption,
              "Location": x.location}

        output[f'Post {i}']= temp
    return output

@app.route('/deleteposts', methods=['Delete'])
def remove1():
    data=request.form
    pid= data.get("post_id")

    present = Post.query.filter_by(post_id=pid).first()
    if not present:
        return make_response("User not present", 202)
    else:
        db.session.delete(present)
        db.session.commit()
        return make_response("User deleted successfully",201)





    # change= data.get("new_name")
    # # print(id, email)
    # if email:
    #     present = User.query.filter_by(email_id=email).first()
    #     if not present:
    #         return make_response("User not present",202)
    #     else:

@app.route('/updatepost', methods=['Put'])
def change1():
    data=request.form
    pid= data.get("post_id")
    col=data.get("change_in")
    new=data.get("new_data")

    present= Post.query.filter_by(post_id= pid).first()
    if not present:
        return make_response("Post not present", 202)
    if col.upper() in ["NAME","LOCATION"]:
        present.col = new
        present.updated_at = datetime.datetime.now()
        present.updated_by = os.getlogin()
        db.session.commit()
        return make_response("Data updated successfully", 201)
    else:
        return make_response("No such Attribute present", 202)


if __name__ == '__main__':
    app.run(port=3600,debug=True)
