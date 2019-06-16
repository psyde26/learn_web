from datetime import datetime 


event_dict =  [
    { 'event_name': 'Серф в Португалии', 'date_start': '10.09.2019', 'date_finish': '21.09.2019', 'country_id': 1, 'type_id':1, 'accomodation': True, 'flight': True, 'meals': True},
   { 'event_name': 'Кайт в Крыму', 'date_start': '21.10.2019', 'date_finish': '11.11.2019', 'country_id': 2, 'type_id':3, 'accomodation': True, 'flight': False, 'meals': True},
   { 'event_name': 'Вейк в Тайланде', 'date_start': '01.02.2020', 'date_finish': '21.02.2020', 'country_id': 3, 'type_id':2, 'accomodation': False, 'flight': False, 'meals': False},
]


country_dict = {
    1: 'Португалия',
    2: 'Россия',
    3: 'Тайланд',
}

type_dict = [
    {'1': 'Cерфинг'},
    {'2': 'Вейк'},
    {'3': 'Кайт'},
]


for event in event_dict:
    event_name = event['event_name']
    
    date_start = datetime.strptime(event['date_start'], '%d.%m.%Y')
    date_finish = datetime.strptime(event['date_finish'], '%d.%m.%Y')
    date_start = date_start.strftime('%d.%m.%Y')
    date_finish = date_finish.strftime('%d.%m.%Y')

    cntr = event['country_id']
    country = country_dict[cntr]

    print(country)


    if event['accomodation'] == True:
        accomodation = 'Включено'
    else:
        accomodation = 'Не включено'
    
    if event['flight'] == True:
        flight = 'Включено'
    else:
        flight = 'Не включено'

    if event['meals'] == True:
        meals = 'Включено'
    else:
        meals = 'Не включено'
    

    print(f'{event_name}, {date_start} - {date_finish} в стране , питане {meals}, перелет {flight}, проживание {accomodation}')