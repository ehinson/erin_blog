from flask import jsonify, request, url_for, abort, current_app
from app import db
from app.models import User, Post
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/search', methods=['GET'])
@token_auth.login_required
def search():
    data = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(data, page, 20)
    data = User.to_collection_dict(posts, page, 20, 'api.search')
    return jsonify(data)

@bp.route('/explore', methods=['GET'])
@token_auth.login_required
def explore():
    data = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(data, page, 20)
    data = User.to_collection_dict(posts, page, 20, 'api.search')
    return jsonify(data)

