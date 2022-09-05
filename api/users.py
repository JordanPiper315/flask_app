from flask import Blueprint, jsonify, abort, request
from ..models import User, db
import unittest

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id:int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'trail_name' not in request.json or 'password' not in request.json:
        return abort(404)
    u = User(
        trail_name = request.json['trail_name'],
        password = request.json['password'],
        address = request.json['address'],
        email = request.json['email'],
        hiking_buddy = request.json['hiking_buddy']
    )
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

class SampleTest(unittest.TestCase):
    def test_get(self):
        self.assertEqual(create(), 404)

if __name__ == '__main__':
    unittest.main()