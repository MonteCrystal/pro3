from flask import request
from flask_login import UserMixin
from server.app.init import db
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash,generate_password_hash


class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER)
    user_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.String(3))
    password = db.Column(db.String(500))
    phone_number = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), primary_key=True)
    records = db.Column(db.INTEGER)
    images = db.Column(db.INTEGER)
    ru = relationship('Record', backref='user_idr')
    iu = relationship('Image', backref='user_idi')
    qu = relationship('query', backref='user_idq')

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password.setter
    # def password(self, password):
    #     """save user name, id and password hash to json file"""
    #     self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
        # return (password==self.password)

    def set(self,username,email):
        self.user_name = username
        self.email = email

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise e

    def register(self, username, password, email):
        try:
            user = User()
            user.set(username, email)
            user.set_password(password)
            user.save()
            return True
        except:
            return False




# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))






class Record(db.Model):
    __tablename__ = 'record'
    record_id = db.Column(db.INTEGER, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'),nullable=False)
    images_befor = db.Column(db.INTEGER)
    images_after = db.Column(db.INTEGER)
    text = db.Column(db.String(1000))

class Image(db.Model):
    __tablename__ = 'image'
    id_address = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'),nullable=False)
    record_id = db.Column(db.INTEGER)
    after_process = db.Column(db.BOOLEAN)
    corresponding_img_id = db.Column(db.String(20))

class algorithm(db.Model):
    __tablename__ = 'algorithm'
    id= db.Column(db.INTEGER, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.TEXT)
    used_time = db.Column(db.INTEGER)
    created = db.Column(db.TIMESTAMP)
    input_type = db.Column(db.TEXT)
    output_type = db.Column(db.TEXT)
    qa = relationship('query', backref='algo_idq')

class query(db.Model):
    __tablename__ = 'query'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'),nullable=False)
    algo_id = db.Column(db.INTEGER,db.ForeignKey('algorithm.id'))
    created = db.Column(db.TIMESTAMP)
    input_addr = db.Column(db.TEXT,nullable=False)
    output_addr = db.Column(db.TEXT,nullable=False)