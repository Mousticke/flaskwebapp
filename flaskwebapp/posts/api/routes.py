from flask import Blueprint, Flask, request, jsonify
from flaskwebapp.models import Post

postsAPI = Blueprint('postsAPI', __name__)

@postsAPI.route('/api/posts', methods=['GET'])
def returnAll():
    posts = Post.query.all()
    postsList = [i.serialize for i in posts]
    return jsonify({'posts': postsList})

@postsAPI.route('/api/posts/<int:post_id>', methods=['GET'])
def returnOne(post_id):
    queryPost = Post.query.filter_by(id=post_id).first()
    post = queryPost.serialize
    return jsonify({'posts': post})