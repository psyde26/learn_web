from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField, DateField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError
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
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})


class CommentForm(FlaskForm):
    event_id = HiddenField('ID события', validators=[DataRequired()])
    comment_text = StringField('Текст комментария', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_event_id(self, event_id):
        if not Event.query.get(event_id.data):
            raise ValidationError('События с таким id не существует')