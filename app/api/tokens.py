from flask import jsonify
from app import db
from app.api import bp
from app.api.auth import basic_auth, token_auth
from datetime import datetime


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    if token:
        basic_auth.current_user().last_seen = datetime.utcnow()
    db.session.commit()
    return jsonify({'token': token, "current_user": basic_auth.current_user().to_dict() })

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204