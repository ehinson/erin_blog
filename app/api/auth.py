from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import jsonify, request, url_for, abort
from app import db
from app.api import bp
from app.models import User
from app.api.errors import error_response
from app.auth.email import send_password_reset_email

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

# basic_auth login required triggers this
# http --auth <username>:<password> POST http://localhost:5000/api/tokens
@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)

# token_auth login required triggers this for API routes
# http GET http://localhost:5000/api/users/1 \
#  "Authorization:Bearer <token>"
@token_auth.verify_token
def verify_token(token):
    return User.check_token(token) if token else None

@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    data = request.get_json() or {}
    user = User.query.filter_by(email=data['email']).first()
    if user:
        send_password_reset_email(user)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
@basic_auth.login_required
def reset_password(token):
    user = User.verify_reset_password_token(token)
    if not user:
        abort(403)
    data = request.get_json() or {}
    user.set_password(data['password'])
    db.session.commit()