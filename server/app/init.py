from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from server.app import config
from flask import Flask, make_response
from flask_login import LoginManager
from flask_mail import Mail
import logging

login_manager = LoginManager()
login_manager.login_view = "user.login"

# app = Flask(__name__,static_folder = "./ocp/static",template_folder = "./dist")
app = Flask(__name__)
login_manager.init_app(app)
app.config.from_object(config)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '234324234'  # 随意设置
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_ECHO'] = True

handler = logging.FileHandler('flask.log')
app.logger.addHandler(handler)


@app.after_request
def after_request(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'content-type,token'
    return resp


mail = Mail()
mail.init_app(app)
