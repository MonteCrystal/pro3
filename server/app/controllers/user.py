import uuid
from flask_mail import Message
from flask import request, jsonify, g, current_app

from server.app.init import mail, app
from server.app.models.model import User, Record, Algorithm

from flask_httpauth import HTTPBasicAuth

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

auth = HTTPBasicAuth()


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
    password = data['password']
    emailAddress = data['emailAddress']
    user = User.query.filter_by(email=emailAddress).first()
    if user is None:
        return jsonify({'code': 400, 'msg': 'error', 'token': ''})
    if user.verify_password(password):
        # login_user(user)
        g.current_user = user
        return jsonify({'code': 200, 'msg': 'ok',
                        'token': user.generate_auth_token(expiration=3600)})
    return jsonify({'code': 400, 'msg': 'error', 'token': ''})


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
    return jsonify({'code': 200, 'msg': 'success', 'data': captcha})


@auth.verify_password
def verify_token(username, client_password):
    username_token = request.headers.get('Token')
    if username_token == '':
        return False
    else:
        g.current_user = _verify_auth_token(username_token)
        g.token_used = True
        return g.current_user is not None


def _verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return None
    return User.query.get(data['id'])


@auth.login_required
def get_record_list():
    objList = g.current_user.my_records
    recordList = []
    for obj in objList:
        recordList.append({
            'id': obj.id,
            'date': str(obj.create_time),
            'name': User.query.get(obj.user_id).user_name,
            'note': obj.description,
        })
    return jsonify({'recordList': recordList})


@auth.login_required
def get_query_list():
    data = request.get_json(silent=True)
    recordId = int(data['recordId'])
    objList = Record.query.filter_by(id=recordId).first().my_queries
    queryList = []
    for obj in objList:
        algo = Algorithm.query.filter_by(id=obj.algo_id).first()
        queryList.append({
            'algo_name': algo.name,
            'algo_desc': algo.description,
            'algo_link': algo.link,
            'input_id_addr': obj.input_id_addr,
            'output_id_addr': obj.output_id_addr
        })
    return jsonify({'queryList': queryList})


@auth.error_handler
def auth_error(status):
    return "Access Denied", status
