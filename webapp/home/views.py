from flask import Blueprint, current_app, render_template

blueprint = Blueprint('home', __name__)   
   
@blueprint.route("/")
def index():
    title = 'Sport application'
    return render_template('home/index.html', page_title=title)