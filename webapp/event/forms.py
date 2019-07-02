from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class EventForm(FlaskForm):
    event_name = StringField(
        'Название события', 
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    date_start = DateField(
        'Дата начала события', 
        validators=[DataRequired()],
        format='%Y-%m-%d',
        render_kw={"class": "form-control"}
    )
    date_finish = DateField(
        'Дата окончания события', 
        validators=[DataRequired()],
        format='%Y-%m-%d',
        render_kw={"class": "form-control"}
        )
    country_id = SelectField(
        u'Страна', 
        validators=[DataRequired()], 
        render_kw={"class": "form-control"}
    )
    type_id = SelectField(
        u'Вид спорта',  
        render_kw={"class": "btn btn-primary"}
    )
    flight = BooleanField(
        'Перелет включен в стоимость',
        default=False, 
        render_kw={"class": "form-check-input"}
    )
    meals = BooleanField(
        'Питание включено в стоимость', 
        default=False, 
        render_kw={"class": "form-check-input"}
    )
    accommodation = BooleanField(
        'Проживание включено в стоимость', 
        default=False, 
        render_kw={"class": "form-check-input"}
    )
    submit = submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})