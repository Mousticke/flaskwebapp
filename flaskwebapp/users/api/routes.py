from flask import Blueprint, Flask, request, jsonify, abort
from flask_api import FlaskAPI, status, exceptions
from flaskwebapp.models import User,Post
from flaskwebapp import bcrypt, db
from sqlalchemy import exc


usersAPI = Blueprint('usersAPI', __name__)

@usersAPI.route('/api/v1/users', methods=['GET'])
def returnAll():
    page = request.args.get('page', None, type=int)
    sorts = request.args.get('sorts', '', type=str)
    username = request.args.get('username', '', type=str)
    email = request.args.get('email', '', type=str)

    if username:
        users = User.query.filter_by(username=username).first()
        if users is None:
            abort(jsonify(devMessage="There is no  with such data in the database", status=400))  
        userList = users.serialize
        return jsonify({'users': userList})
    elif email:
        users = User.query.filter_by(email=email).first()
        if users is None:
            abort(jsonify(devMessage="There is no  with such data in the database", status=400))          
        userList = users.serialize
        return jsonify({'users': userList})
    elif username and email:
        users = User.query.filter_by(email=email, username=username).first()
        if users is None:
            abort(jsonify(devMessage="There is no  with such data in the database", status=400))          
        userList = users.serialize
        return jsonify({'users': userList})

    if page and sorts is None:
        users = User.query.all()
    elif sorts is None:
        users = User.query.paginate(page=page, per_page=2).items
    elif page is None:
        if sorts == 'rank_asc':
            users = User.query.order_by(User.username.asc()).all()
        else:
            users = User.query.order_by(User.username.desc()).all()
    else:
        if sorts == 'rank_asc':
            users = User.query.order_by(User.username.asc()).paginate(page=page, per_page=2).items
        else:
            users = User.query.order_by(User.username.desc()).paginate(page=page, per_page=2).items
    if users is None:
        abort(jsonify(devMessage="There is no user in the database", status=400))
    else:
        usersLists = [i.serialize for i in users]
        return jsonify({'users': usersLists})

@usersAPI.route('/api/v1/users/<int:user_id>', methods=['GET'])
def returnOne(user_id):
    queryUser = User.query.filter_by(id=user_id).first()
    if queryUser is None:
        abort(jsonify(devMessage="There is no user with this id in the database", status=400))
    else:
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
        abort(jsonify(devMessage="Can't add this user. This user alread exist", status="409"))

    return jsonify({'users': userObject, 'status': '200'})

@usersAPI.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
def returnAllPosts(user_id):
    
    page = request.args.get('page', None, type=int)
    sorts = request.args.get('sorts', '', type=str)

    usersPost = User.query.filter_by(id=user_id).first()
    if usersPost is None:
        abort(jsonify(devMessage="There is no user in the database", status=400))
    
    if page and sorts is None:
        posts = Post.query.filter_by(author=usersPost).all()
    elif sorts is None:
        posts = Post.query.filter_by(author=usersPost).paginate(page=page, per_page=2).items
    elif page is None:
        if sorts == 'rank_asc':
            posts = Post.query.filter_by(author=usersPost).order_by(Post.date_posted.asc())            
        else:
            posts = Post.query.filter_by(author=usersPost).order_by(Post.date_posted.desc())
    else:
        if sorts == 'rank_asc':
           posts = Post.query.filter_by(author=usersPost).order_by(Post.date_posted.asc()).paginate(page=page, per_page=2).items
        else:
            posts = Post.query.filter_by(author=usersPost).order_by(Post.date_posted.desc()).paginate(page=page, per_page=2).items
    if posts is None:
        abort(jsonify(devMessage="There is no posts for this user with the argument passed", status=400))
    else:
        postsList = [i.serialize for i in posts]
        return jsonify({'posts': postsList})

@usersAPI.route('/api/v1/users/<int:user_id>/posts/<int:post_id>', methods=['GET'])
def returnOnePosts(user_id, post_id):
    usersPost = User.query.filter_by(id=user_id).first()
    if usersPost is None:
        abort(jsonify(devMessage="There is no user in the database", status=400))
    postItem = Post.query.filter_by(author=usersPost, id=post_id).first()
    if postItem is None:
        abort(jsonify(devMessage="There is no post for this user in the database", status=400))
    post = postItem.serialize
    return jsonify({'posts': post})
    