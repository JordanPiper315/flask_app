from flask import Blueprint, jsonify, abort, request
from ..models import Gear, db
import unittest

bp = Blueprint('gear', __name__, url_prefix='/gear')


@bp.route('', methods=['GET'])
def index():
    gear = Gear.query.all()
    result = []
    for g in gear:
        result.append(g.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    g = Gear.query.get_or_404(id)
    return jsonify(g.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(404)
    g = Gear(
        name=request.json['name'],
        weight=request.json['weight'],
        trip_id=request.json['trip_id'],
    )
    db.session.add(g)
    db.session.commit()
    return jsonify(g.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    g = Gear.query.get_or_404(id)
    try:
        db.session.delete(g)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

class SampleTest(unittest.TestCase):
    def test_get(self):
        self.assertEqual(create(), 404)

if __name__ == '__main__':
    unittest.main()
