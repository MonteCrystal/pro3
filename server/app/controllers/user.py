import uuid
from flask_mail import Message
from flask import request, jsonify
# from flask_login import current_user
# from werkzeug.utils import redirect


# from server.app.init import app
from flask_login import login_user

from server.app.init import mail
from server.app.models.model import User


# @app.route('/register', methods=['POST'])
def register():
    user = User()
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    emailAddress = data['emailAddress']
    # password = request.json.get('password')
    # email = request.json.get('emailAddress')
    try:

        user.set(username, emailAddress)
        user.set_password(password)
        user.save()
        return jsonify({'code': 200, 'msg': 'success'})
    except Exception as e:
        return jsonify({'code': 400, 'msg': 'error'})

        

def login():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    emailAddress = data['emailAddress']
    user = User.query.filter(User.email == emailAddress).first()
    if user.verify_password(password):
        login_user(user)
        return jsonify({'code': 200, 'msg': 'success'})
    return jsonify({'code': 400, 'msg': 'error'})



def email_captcha():
    data = request.get_json(silent=True)
    email = data['emailAddress']
    # if not email:
    #     return restful.params_error('请输入邮箱')  #restful. 封装的函数，返回前端数据
    '''
    生成随机验证码，保存到memcache中，然后发送验证码，与用户提交的验证码对比
    '''
    captcha = str(uuid.uuid1())[:6]  # 随机生成6位验证码
    # 给用户提交的邮箱发送邮件
    message = Message('云平台验证码：', recipients=[email], body='您的验证码是：%s' % captcha)
    try:
        mail.send(message)  # 发送
    except:
        return jsonify({'code': 400, 'msg': 'error'})
        # return restful.server_error()
    # mbcache.set(email, captcha)
    # return restful.success()
    return jsonify({'code': 200, 'msg': 'success','data':captcha})
