from flask import jsonify, request, url_for, abort
from app import db, current_app
from app.models import User
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth
import os


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict(token_auth.current_user()))


@bp.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>/followers', methods=['GET'])
def get_followers(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followers, page, per_page,
                                   'api.get_followers', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/posts', methods=['GET'])
def get_user_posts(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.posts, page, per_page,
                                   'api.get_user_posts', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/followed', methods=['GET'])
def get_followed(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followed, page, per_page,
                                   'api.get_followed', id=id)
    return jsonify(data)


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.form.to_dict() or {}
    user = User()

    if request.files:
        image = request.files["file"]
        image.save(os.path.join(
            current_app.config["IMAGE_UPLOADS"], image.filename))
        user.image_url = image.filename

    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')

    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict(current_user=None))
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    if token_auth.current_user().id != id:
        abort(403)
    user = User.query.get_or_404(id)
    data = request.form.to_dict() or {}
    if request.files:
        image = request.files["file"] or request.files
        image.save(os.path.join(
            current_app.config["IMAGE_UPLOADS"], image.filename))
        user.image_url = image.filename
    else:
        user.image_url = ''
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict(token_auth.current_user()))


@bp.route('/follow/<int:id>', methods=['POST'])
@token_auth.login_required
def follow(id):
    user = User.query.get_or_404(id)
    if user is None:
        return bad_request('User does not exist')
    if user == token_auth.current_user():
        return bad_request('You cannot follow yourself')
    token_auth.current_user().follow(user)

    db.session.commit()
    return jsonify(user.to_dict(token_auth.current_user()))


@bp.route('/unfollow/<int:id>', methods=['POST'])
@token_auth.login_required
def unfollow(id):
    user = User.query.get_or_404(id)
    if user is None:
        return bad_request('User does not exist')
    if user == token_auth.current_user():
        return bad_request('You cannot unfollow yourself')

    token_auth.current_user().unfollow(user)
    db.session.commit()
    return jsonify(user.to_dict(token_auth.current_user()))
