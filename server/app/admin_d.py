from flask import Blueprint

admin_d = Blueprint('admin_d',__name__)



@admin_d.route('/add')
def add():
    return 'user_add'

@admin_d.route('/show')
def show():
    return 'user_show'