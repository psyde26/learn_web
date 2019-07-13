from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask_login import current_user, login_required

from webapp.event.forms import EventForm, AllEventsForm
from webapp.event.models import Event, Type, Country, db, UserEvent


blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/', methods = ['GET'])
def event():
    title = 'Предстоящие события'
    form = AllEventsForm()
    all_events = Event.query.all()
    subscribed_events = set(item.event_id for item in UserEvent.query.filter(UserEvent.user_id==current_user.id))
    return render_template('event/index.html', page_title=title, form=form, all_events=all_events, subscribed_events=subscribed_events)

@blueprint.route('/new-event', methods=['GET'])
def new_event():
    title = 'Новое событие'
    form = EventForm()
    form.country_id.choices = [(country.id, country.country_name) for country in Country.query.order_by('country_name')]
    form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]
    return render_template('event/create_event.html', page_title=title, form=form)

@login_required
@blueprint.route('/create-event', methods=['POST'])
def create_event():
    form = EventForm()
    form.country_id.choices = [(country.id, country.country_name) for country in Country.query.order_by('country_name')]
    form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]

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

@blueprint.route('/<int:ev_id>/subscribe', methods=['GET'])
def subscribe(ev_id):
    print(ev_id)
    new_subscribe = UserEvent(
            user_id = current_user.id,
            event_id = ev_id
    )
    db.session.add(new_subscribe)
    db.session.commit()
    flash('Вы подписались на событие')
    return redirect(url_for('event.event'))


@blueprint.route('/<int:uns_ev_id>/unsubscribe', methods=['GET'])
def unsubscribe(uns_ev_id):
    print('uns = {uns_ev_id}')
    unsubscribe = UserEvent.query.filter_by(event_id=uns_ev_id, user_id=current_user.id).delete()
    # UserEvent.user_id = 0
    # UserEvent.event_id = 0   
   
  
    db.session.commit()
    flash('Вы отписались от события')
    return redirect(url_for('event.event'))

 

    #flash('Пожалуйста, исправьте ошибки в форме')
    #return redirect('new-event')
