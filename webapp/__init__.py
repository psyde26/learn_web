from flask import Flask, render_template

from webapp.model import db, Event, Type, Country


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py') 
    db.init_app(app)

    return app