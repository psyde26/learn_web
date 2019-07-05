from flask import Blueprint, current_app, render_template

from webapp.event.models import Country, Type, Event

blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/')
def event():
    # context = {
    #     'page_title': "Все события",
    #     'events_list': Event.query.get('event_name')
    # }

    page_title = "Все события"
    events_list = Event.query.all()

    return render_template('event/index.html', events_list=events_list)