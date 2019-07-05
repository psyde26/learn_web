# -*- coding: utf-8 -*-

from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    username = input('Введите имя:')

    if User.query.filter(User.username == username).count():
        print('пользователь с таким именем уже существует')
        sys.exit(0)

    password1 = getpass('введите пароль')
    password2 = getpass('Повторите пароль')

    if not password1 == password2:
        print('Пароли не одинаковые')
        sys.exit(0)


    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()

    print('Пользователь с id {} добавлен'.format(new_user.id))
    