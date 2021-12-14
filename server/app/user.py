from flask import Blueprint

user = Blueprint('user',__name__)



@user.route('/add')
def add():
    return 'user_add'

@user.route('/show')
def show():
    return 'user_show'