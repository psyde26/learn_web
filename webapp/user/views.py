from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask_login import login_required, login_user, logout_user, current_user

from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp.userevent.models import UserEvent
from webapp.event.models import Event, Country, Type
from webapp import db

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно вошли на сайт')
            return redirect(url_for('home.index'))

    flash('Неправильное имя или пароль')
    return redirect('user.login')

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))
    flash('Вы успешно разлогинились')

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    title = 'Регистрация'
    form = RegistrationForm()
    return render_template('user/registration.html', page_title = title, form = form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data,
        role = 'user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('user.login'))

    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect('user.register')

@blueprint.route('/subscriptions', methods=['GET'])
def user_subscriptions():
    title = 'Ваши подписки'
    event_list = Event.query.all()
    subscribed_events = set(item.event_id for item in UserEvent.query.filter(UserEvent.user_id==current_user.id))
    return render_template(
        'user/subscriptions.html', 
        page_title=title, 
        event_list=event_list,
        subscribed_events=subscribed_events)

@blueprint.route('/<int:uns_ev_id>/unsubscribe', methods=['GET'])
def unsubscribe(uns_ev_id):
    print('uns = {uns_ev_id}')
    unsubscribe = UserEvent.query.filter_by(event_id=uns_ev_id, user_id=current_user.id).delete()
  
    db.session.commit()
    flash('Вы отписались от события')
    return redirect(url_for('user.user_subscriptions'))
    