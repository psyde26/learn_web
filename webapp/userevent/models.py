from flask_login import UserMixin

from webapp.db import db

class UserEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sub_user = db.relationship('User', backref='sub_user')
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    sub_event = db.relationship('Event', backref='sub_event')

    def __repr__(self):
        return '<UserEvent {} {}>'.format(self.user_id, 
        self.event_id)
        