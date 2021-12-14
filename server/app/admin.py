from flask import Blueprint

admin = Blueprint('admin',__name__)



@admin.route('/add')
def add():
    return 'user_add'

@admin.route('/show')
def show():
    return 'user_show'