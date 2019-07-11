from flask import Flask, render_template, flash, redirect, url_for, Blueprint, request
from flask_login import current_user, login_required
from datetime import datetime

from webapp.event.forms import EventForm
from webapp.event.models import Event, Type, Country, db
from webapp.userevent.models import UserEvent
from webapp.user.decorators import admin_required


blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/', methods = ['GET'])
def event():
    title = 'Предстоящие события'
    events_list = Event.query.all()
    return render_template('event/index.html', page_title=title, events_list=events_list)
    

@blueprint.route('/new-event', methods=['GET'])
@admin_required
def new_event():
    title = 'Новое событие'
    title2 = 'Все доступные события'
    form = EventForm()
    events_list = Event.query.all()
    form.country_id.choices = [(country.id, country.country_name) for country in Country.query.order_by('country_name')]
    form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]
    return render_template(
        'event/create_event.html', 
        page_title=title, 
        page_title2 = title2, 
        form=form,
        events_list=events_list
    )

@blueprint.route('/create-event', methods=['POST'])
@admin_required
def create_event():
    form = EventForm()
    form.country_id.choices = [
        (country.id, country.country_name) for country in Country.query.order_by('country_name')
    ]
    form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]

    if form.validate_on_submit():
        new_event = Event(
            event_name = form.event_name.data,
            date_start = form.date_start.data,
            date_finish = form.date_finish.data,
            country_id = int(form.country_id.data),
            type_id = int(form.type_id.data),
            flight = form.flight.data,
            meals = form.meals.data,
            accommodation = form.accommodation.data,
            event_creator_id = current_user.id
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Создано новое событие')
        return redirect(url_for('event.event'))

    flash('Пожалуйста, исправьте ошибки в форме')
    print(form.errors.items())
    title = 'Новое событие'
    return render_template('event/create_event.html', page_title=title, form=form)

@blueprint.route('/all-events', methods=['GET'])
@admin_required
def all_events():
    title2 = 'Все доступные события'
    events_list = Event.query.all()
    return render_template(
        'event/all_events.html', 
        page_title2 = title2, 
        events_list=events_list
    )

@blueprint.route('/<int:ev_id>/subscribe', methods=['GET'])
def subscribe(ev_id):

    new_subscribe = UserEvent(
            user_id = current_user.id,
            event_id = ev_id
    )
    db.session.add(new_subscribe)
    db.session.commit()
    flash('Вы подписались на событие')
    return redirect(url_for('event.event'))

@blueprint.route('/edit/<int:id>', methods=["POST", "GET"])
def update_record(id):
    events_list = Event.query.all()
    if request.method == "POST":
        event_name = request.form["event_name"]
        date_start = datetime.strptime(request.form['date_start'], '%d-%m-%Y')
        date_finish = datetime.strptime(request.form['date_finish'], '%d-%m-%Y')
        country_id = request.form['country_id']
        type_id = request.form["type_id"]
        flight = request.form['flight']
        meals = request.form['meals']
        accommodation = request.form['accommodation']

        update_event = Event.query.get(id)
        update_event.event_name = event_name
        update_event.date_start = date_start
        update_event.date_finish = date_finish
        update_event.country_id = country_id
        update_event.type_id = type_id
        update_event.flight = flight
        update_event.meals = meals
        update_event.accommodation = accommodation

        db_session.commit()

        return redirect(url_for("/all-event"))
    else:
        new_event = Event.query.get(id)
        new_event.event_name = new_event.event_name
        new_event.date_start = new_event.date_start
        new_event.date_finish = new_event.date_finish
        new_event.country_id = new_event.country_id
        new_event.type_id = new_event.type_id
        new_event.flight = new_event.flight
        new_event.meals = new_event.meals
        new_event.accommodation = new_event.accommodation

        return render_template('event/update_event.html', data=new_event, events_list=events_list)
