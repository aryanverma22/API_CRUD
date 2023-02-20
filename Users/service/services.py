import json
import datetime
import os

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, ForeignKey



def read(db,User):
    '''
        Returns all the Users in the users table.
        :param db:
        :param User:
        :return:
        '''
    # trial= User(name= ' Aryan',id= 4)
    db.create_all()
    # db.session.delete()
    # db.session.add(trial)
    # User.query.filter_by(id = 4).delete()
    db.session.commit()

    data = User.query.all()

    out=[]
    print(data[1])
    i=0
    for x in data:
        i+=1
        temp={'ID': x.id,
              'Name': x.name,
              'Email_id': x.email_id}
        out.append(temp)
    final={'data': out,
           'message':'Data returned successfully'}
    return make_response(final,201)

def create(db,User):
    '''
    Creates a new entry in the Usere database by taking Json input('name,'email') from the API and returns the status message
    :param db:
    :param User:
    :return:
    '''
    data= request.json
    name1= data["name"]
    email1= data["email"]

    present = User.query.filter_by(email_id= email1).first()
    new = User(name=name1, email_id=email1)
    if not present:

        db.session.add(new)
        db.session.commit()
        final={'data': f" ('ID: {new.id}', 'name: {new.name}', 'email_id: {new.email_id}')",
               'message': "User successfully added"}
        return make_response(final,201)
    else:
        final = { 'data': f" ('ID: {new.id}', 'name: {new.name}', 'email_id: {new.email_id}')",
                 'message': "User already present"}
        return make_response(final,404)

def update_user(db,User):
    '''
    Updates the users corresponding to the 'user_id', 'change_in', 'new_data' being provided as a Json input.
    :param db:
    :param User:
    :return:
    '''
    data= request.json
    user_id= data["user_id"]
    col_to_change= data["change_in"]
    new= data["new_data"]
    present = User.query.filter_by(id=user_id).first()
    if not present:
        return make_response({'Data': data,"message":"User not present"},404)
    else:
        if col_to_change == "email":
            present1 = User.query.filter_by(email_id= new).first()
            print(present1)
            if present1:
                return make_response({'Data': data,'message':"Email already registered"}, 405)
            else:
                present.email_id= new
                present.updated_at= datetime.datetime.now()
                present.updated_by= os.getlogin()
                db.session.commit()
                final = {'data': f" ('ID: {present.id}', 'name: {present.name}', 'email_id: {present.email_id}')",
                         'message': "Data updated successfully"}
                return make_response(final,201)
        elif col_to_change == "name":
            present.name = new
            present.updated_at = datetime.datetime.now()
            present.updated_by = os.getlogin()
            db.session.commit()
            final = {'data': f" ('ID: {present.id}', 'name: {present.name}', 'email_id: {present.email_id}')",
                     'message': "Data updated successfully"}
            return make_response(final, 201)
        else:
            return make_response({'Data': data,'Message':"No such Attribute present"}, 404)

def delete(db,User):
    '''
    Deletes the record corresponding to the 'user_id' being taken as a Json input.
    :param db:
    :param User:
    :return:
    '''
    data=request.json
    uid= data["user_id"]
    print(uid)
    present = User.query.filter_by(id=uid).first()
    if not present:
        return make_response({'Data': data, 'message':"User_id not valid"}, 404)
    else:
        db.session.delete(present)
        db.session.commit()

        final={'data': f" ('ID: {present.id}', 'name: {present.name}', 'email_id: {present.email_id}')",
               'message':"User deleted successfully" }
        return make_response(final,201)





    # change= data.get("new_name")
    # # print(id, email)
    # if email:
    #     present = User.query.filter_by(email_id=email).first()
    #     if not present:
    #         return make_response("User not present",202)
    #     else: