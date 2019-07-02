from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask_login import current_user

from webapp.event.forms import EventForm
from webapp.event.models import Event, Type, Country
from webapp import db

blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/')
def event():
    title = 'Последние события'
    return render_template('event/index.html', page_title=title)

@blueprint.route('/new-event')
def new_event():
    title = 'Последние события'
    form = EventForm()
    form.country_id.choices = [(country.id, country.country_name) for country in Country.query.order_by('country_name')]
    form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]
    return render_template('event/create_event.html', page_title=title, form=form)

@blueprint.route('/create-event', methods=['POST'])
def create_event():
    form = EventForm()

    if form.validate_on_submit():
        new_event = Event(
            event_name = form.event_name.data,
            date_start = form.date_start.data,
            date_finish = form.date_finish.data,
            country_id = form.country_id.data,
            type_id = form.type_id.data,
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
    return redirect('event.new-event')
