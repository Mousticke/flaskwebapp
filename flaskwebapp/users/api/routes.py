from flask import Blueprint, Flask, request, jsonify, abort
from flask_api import FlaskAPI, status, exceptions
from flaskwebapp.models import User
from flaskwebapp import bcrypt, db
from sqlalchemy import exc


usersAPI = Blueprint('usersAPI', __name__)

@usersAPI.route('/api/v1/users', methods=['GET'])
def returnAll():
    users = User.query.all()
    usersLists = [i.serialize for i in users]
    return jsonify({'users': usersLists})

@usersAPI.route('/api/v1/users/<int:user_id>', methods=['GET'])
def returnOne(user_id):
    queryUser = User.query.filter_by(id=user_id).first()
    user = queryUser.serialize
    return jsonify({'users': user})

@usersAPI.route('/api/v1/users', methods=['POST'])
def addOne():
    if not request.json or not 'email' or not 'password' or not 'username' or not 'confirm_password' in request.json:
        abort(jsonify(devMessage="One or more filed are missing", status="400"))

    if request.json['password'] != request.json['confirm_password']:
        abort(jsonify(devMessage="Password are not the same", status="400"))

    hashed_pwd = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
    userObject = {'username': request.json['username'], 'email': request.json['email'], 'password': hashed_pwd}
    
    user = User(username=request.json['username'], email=request.json['email'], password=hashed_pwd)
    db.session.add(user)
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        abort(jsonify(devMessage="Can't add this user. This user alread exist", status="400"))

    return jsonify({'users': userObject, 'status': '200'})