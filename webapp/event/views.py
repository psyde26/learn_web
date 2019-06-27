from flask import Blueprint, current_app, render_template

blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/')
def event():
    title = 'Последние события'
    return render_template('event/index.html', page_title=title)