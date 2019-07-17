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
    subscribed_events = set(item.event_id for item in UserEvent.query.filter(UserEvent.user_id==current_user.id))
    return render_template(
        'event/index.html', 
        page_title=title, 
        events_list=events_list,
        subscribed_events=subscribed_events,
    )
    

@blueprint.route('/new', methods=['GET', 'POST'])
@blueprint.route('/edit/<int:ev_id>', methods=['GET', 'POST'])
def new_event(ev_id=None):
    title = 'Редактировать событие' if ev_id else 'Новое событие'
    form = EventForm()
    form.country_id.choices = [
    (country.id, country.country_name) for country in Country.query.order_by('country_name')
]
    form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]
    if request.method == 'GET':
        if ev_id:
            form = EventForm(obj=Event.query.get(ev_id))
 
        form.country_id.choices = [
            (country.id, country.country_name) for country in Country.query.order_by('country_name')
        ]
        form.type_id.choices = [(t.id, t.sport_name) for t in Type.query.order_by('sport_name')]

        return render_template(
            'event/create_event.html', 
            page_title=title,
            form=form,
        )
    
    else:
        if form.validate_on_submit():
            if ev_id:
                event = Event.query.get(ev_id)
                msg = 'Событие обновлено'
            else:
                event = Event()
                msg = 'Создано новое событие'

            event.event_name = form.event_name.data
            event.date_start = form.date_start.data
            event.date_finish = form.date_finish.data
            event.country_id = int(form.country_id.data)
            event.type_id = int(form.type_id.data)
            event.flight = form.flight.data
            event.meals = form.meals.data
            event.accommodation = form.accommodation.data
            event.event_creator_id = current_user.id
            db.session.add(event)
            db.session.commit()
            flash(msg)
            return redirect(url_for('event.event'))

        flash('Пожалуйста, исправьте ошибки в форме')
        return render_template(
            'event/create_event.html', 
            page_title=title, 
            form=form
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

@blueprint.route('/<int:uns_ev_id>/unsubscribe', methods=['GET'])
def unsubscribe(uns_ev_id):
    print('uns = {uns_ev_id}')
    unsubscribe = UserEvent.query.filter_by(event_id=uns_ev_id, user_id=current_user.id).delete()
  
    db.session.commit()
    flash('Вы отписались от события')
    return redirect(url_for('event.event'))

@blueprint.route('/<int:ev_id>/delete', methods=['GET'])
def delete_event(ev_id):

    obj=Event.query.get(ev_id)
    
    db.session.delete(obj)
    db.session.commit()
    flash('Событие удалено')
    return redirect(url_for('event.event'))
