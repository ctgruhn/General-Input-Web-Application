from datetime import datetime
from hazardapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)    # may need to extend limit for longer names
    last_name = db.Column(db.String(20), nullable=False)     # may need to extend limit for longer names
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    hazards = db.relationship('Hazards', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.first_name}','{self.last_name}' '{self.email}')"

class Hazards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    task = db.Column(db.String(120), nullable=False)
    hazard = db.Column(db.String(20), nullable=False)
    details = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Hazard('{self.area}', '{self.location}', '{self.task}', '{self.hazard}', '{self.date_submitted}')"