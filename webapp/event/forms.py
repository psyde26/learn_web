from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField, SelectField, IntegerField, HiddenField, TextField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields.html5 import DateField

from webapp.event.models import Event, Type, Country, db, Comment

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
        'Страна',
        coerce=int,
        validators=[DataRequired()], 
        render_kw={"class": "form-control"}
    )
    type_id = SelectField(
        'Вид спорта',
        coerce=int,
        validators=[DataRequired()],  
        render_kw={"class": "form-control"}
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
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-dark"})

class CommentForm(FlaskForm):
    event_id = HiddenField('ID события')
    comment_text = StringField('Текст комментария', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-dark"})
