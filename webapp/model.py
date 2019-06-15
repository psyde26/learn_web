from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String, nullable=False)
    events = db.relationship('Event', backref='country', lazy=True)

    def __repr__(self):
        return '<Country {}>'.format(self.county_name)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport_name = db.Column(db.String, nullable=False)
    types = db.relationship('Event', backref='type', lazy=True) 

    def __repr__(self):
        return '<Type {}>'.format(self.sport_name)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)
    date_finish = db.Column(db.DateTime, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), 
    nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    flight = db.Column(db.Boolean, nullable=False)
    meals = db.Column(db.Boolean, nullable=False)
    accommodation = db.Column(db.Boolean, nullable=False)    

    def __repr__(self):
        return '<Event {} {} {} {} {} {} {} {}>'.format(self.event_name, 
        self.date_start, self.date_finish, self.country_id, self.type_id, 
        self.flight, self.meals, self.accommodation)
        