from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trail_name = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128))
    email = db.Column(db.String(128))
    hiking_buddy = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    trips = db.relationship('Trip', backref='user')
    def __init__(self, trail_name: str, password: str, address=None, email=None, hiking_buddy=None):
        self.trail_name = trail_name
        self.password = password
        self.address = address
        self.email = email
        self.hiking_buddy = hiking_buddy
    def serialize(self):
        return {
            'id': self.id,
            'trail_name': self.trail_name,
            'password': self.password,
            'address': self.address,
            'email': self.email,
            'hiking_buddy': self.hiking_buddy
        }

users_gear = db.Table(
    'users_gear',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('gear_id', db.Integer, db.ForeignKey('gear.id'), primary_key=True)
)

class Gear(db.Model):
    __tablename__ = 'gear'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    weight = db.Column(db.Integer)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    def __init__(self, name: str, weight: int, trip_id: int):
       self.name = name
       self.weight = weight
       self.trip_id = trip_id
    def serialize(self):
        return {
            'name': self.name,
            'weight': self.weight,
            'trip_id': self.trip_id,
        }