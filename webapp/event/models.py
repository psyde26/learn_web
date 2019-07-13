from flask import url_for
from flask_login import UserMixin
from datetime import date

from webapp.db import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String, nullable=False)
    events = db.relationship('Event', backref='country', lazy=True)

    def __repr__(self):
        return '<Country {}>'.format(self.country_name)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport_name = db.Column(db.String, nullable=False)
    types = db.relationship('Event', backref='type', lazy=True) 

    def __repr__(self):
        return '<Type {}>'.format(self.sport_name)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    date_start = db.Column(db.DateTime)
    date_finish = db.Column(db.DateTime)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), 
    nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    flight = db.Column(db.Boolean, nullable=False)
    meals = db.Column(db.Boolean, nullable=False)
    accommodation = db.Column(db.Boolean, nullable=False)  
    event_creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_creator = db.relationship('User', backref='created_events')

    def __repr__(self):
        return '<Event {} {} {} {} {} {} {} {} {}>'.format(self.event_name, 
        self.date_start, self.date_finish, self.country_id, self.type_id, 
        self.flight, self.meals, self.accommodation, self.event_creator_id)
    
    @property
    def subscribe_link(self):
        if self.id:
            return url_for('event.subscribe', ev_id=self.id)

    @property
    def unsubscribe_link(self):
        if self.id:
            return url_for('event.unsubscribe', uns_ev_id=self.id)
    

#Subscribe
class UserEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sub_user = db.relationship('User', backref='sub_user')
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    sub_event = db.relationship('Event', backref='sub_event')

    def repr(self):
        return '<UserEvent {} {}>'.format(self.user_id, 
        self.event_id)
        