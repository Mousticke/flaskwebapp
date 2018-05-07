from flask import Blueprint, Flask, request, jsonify
from flaskwebapp.models import User

usersAPI = Blueprint('usersAPI', __name__)

@usersAPI.route('/api/users', methods=['GET'])
def returnAll():
    users = User.query.all()
    usersLists = [i.serialize for i in users]
    return jsonify({'users': usersLists})

@usersAPI.route('/api/users/<int:user_id>', methods=['GET'])
def returnOne(user_id):
    queryUser = User.query.filter_by(id=user_id).first()
    user = queryUser.serialize
    return jsonify({'users': user})