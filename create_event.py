from datetime import date

from webapp import create_app
from webapp.model import db, Event, Type, Country


app = create_app()


with app.app_context():
    event_name = input("Название события: ")

    str_date_start = input("Дата начала: ")
    date_start = date.strptime(str_date_start, '%d/%m/%y')

    str_date_finish = input("Дата окончания: ")
    date_finish = date.strptime(str_date_finish, '%d/%m/%y')


    new_event = Event(event_name=event_name, 
    date_start = date_start,
    date_finish=date_finish,
    country_id = 'Россия',
    type_id = 'Кайт',
    flight = True,
    meals = True,
    accommodation = True)

    db.session.add(new_event)
    db.session.commit()
    print('Создан новый эвент с id={}'.format(new_event.id))
