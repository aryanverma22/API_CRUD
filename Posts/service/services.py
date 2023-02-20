import json
import datetime
import os

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



def create(db,Post,User):
    '''
    Creates a new entry in the Posts database by taking Json input('Caption','User_id','location') from the API and returns the status message.
    :param db:
    :param Post:
    :param User:
    :return:
    '''

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
    return make_response({'Data': data, 'Message': out})

    # cap= data.get("caption")
    # userid= data.get("user_id")
    # new = Post(user_id= userid, caption=cap)
    # db.session.add(new)
    # db.session.commit()
    # return make_response("jjk")

def read(db,Post):
    '''
    Returns the Posts corresponding to the 'user_id' being provided as a Json input
    :param db:
    :param Post:
    :return:
    '''
    data=request.json
    uid=data["User_id"]
    present = Post.query.filter_by(user_id=uid)
    if not present:
        return make_response({ 'Data': data
                  ,'Message':"No posts found"},404)

    output={}
    li=[]
    i=0
    for x in present:
        i+=1
        temp={}
        print((x))
        temp={"Post_ID": x.post_id,
              "User_ID": x.user_id,
              "Caption": x.caption,
              "Location": x.location}
        li.append(temp)
    output={'Data': li,"Message":"Posts returned successfully"}
    return make_response(output, 201)

def delete(db,Post):
    '''
    Deletes the record corresponding to the 'post_id' being taken as a Json input
    :param db:
    :param Post:
    :return:
    '''
    data=request.json
    pid= int(data["post_id"])

    present = Post.query.filter_by(post_id=pid).first()
    if not present:
        return make_response({"Data": data,
            'Message':"Post_id not valid"}, 404)
    else:
        db.session.delete(present)
        db.session.commit()
        return make_response({'data': f" ('Post_ID: {present.post_id}', 'User_id: {present.user_id}', 'Caption: {present.caption}','Location:{present.location}')",
                             "Message":"Post deleted successfully"},201)





    # change= data.get("new_name")
    # # print(id, email)
    # if email:
    #     present = User.query.filter_by(email_id=email).first()
    #     if not present:
    #         return make_response("User not present",202)
    #     else:

def update_post(db,Post):
    '''
    Updates the posts corresponding to the 'post_id', 'change_in', 'new_data' being provided as a Json input.
    :param db:
    :param Post:
    :return:
    '''
    data=request.json
    pid= data["post_id"]
    col=data["change_in"]
    new=data["new_data"]

    present= Post.query.filter_by(post_id= pid).first()
    if not present:
        return make_response({"Data": data, 'message':"Post not present"}, 404)
    if col.upper() in ["CAPTION","LOCATION"]:
        present.col = new
        present.updated_at = datetime.datetime.now()
        present.updated_by = os.getlogin()
        db.session.commit()
        return make_response({'Data': data,
            'Message':"Data updated successfully"}, 201)
    else:
        return make_response({"Data":data, 'Message':"No such Attribute present"}, 404)
