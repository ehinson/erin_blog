from flask import jsonify, request, url_for
from app import db, current_app
from app.models import Post
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth
import os

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    return jsonify(Post.query.get_or_404(id).to_dict())

@bp.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Post.to_collection_dict(Post.query, page, per_page, 'api.get_posts')
    return jsonify(data)

@bp.route('/posts/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json() or {}
    post.from_dict(data)
    db.session.commit()
    return jsonify(post.to_dict(token_auth.current_user()))

@bp.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    data = request.form.to_dict() or {}
    if request.files:
      image = request.files["file"]
      image.save(os.path.join(current_app.config["IMAGE_UPLOADS"], image.filename)) 
    if 'title' not in data or 'body' not in data:
        return bad_request('must include title and body fields')
    post = Post()
    post.user_id = token_auth.current_user().id
    post.from_dict(data)
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict(token_auth.current_user()))
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response
