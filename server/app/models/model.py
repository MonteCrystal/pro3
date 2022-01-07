import os

from flask import current_app
from flask_httpauth import HTTPBasicAuth
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import func
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from server.app.init import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER,
                   autoincrement=True,
                   primary_key=True,
                   nullable=False)
    user_name = db.Column(db.String(30),
                          nullable=False)
    password = db.Column(db.String(500),
                         nullable=False)
    email = db.Column(db.String(50),
                      nullable=False,
                      unique=True)
    age = db.Column(db.String(3))
    phone_number = db.Column(db.String(15))
    gender = db.Column(db.TEXT)
    address = db.Column(db.String(100))
    left_eyesight = db.Column(db.String(4))
    right_eyesight = db.Column(db.String(4))

    my_records = relationship('Record', back_populates='record_usr')
    my_dataobjs = relationship('DataObj', back_populates='data_usr')
    my_algorithms = relationship('Algorithm', back_populates='algo_usr')

    auth = HTTPBasicAuth()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    def verify_password(self, input_pwd):
        return check_password_hash(self.password, input_pwd)

    def set(self, username, email):
        self.id = 0
        self.user_name = username
        self.email = email
        self.age = '/'
        self.phone_number = '/'
        self.gender = 'Prefer not to respond'
        self.address = '/'
        self.left_eyesight = '0.0'
        self.right_eyesight = '0.0'

    def set_user_info(self, userInfo):
        self.user_name = userInfo['name']
        self.email = userInfo['email']
        self.age = userInfo['age']
        self.phone_number = userInfo['phone']
        self.gender = userInfo['gender']
        self.address = userInfo['address']
        self.left_eyesight = userInfo['left_eyesight']
        self.right_eyesight = userInfo['right_eyesight']
        self.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise e

    @staticmethod
    def register(username, password, email):
        try:
            user = User()
            user.set(username, email)
            user.set_password(password)
            user.save()
            return True
        except:
            return False


class DataObj(db.Model):
    __tablename__ = 'dataobjs'
    id = db.Column(db.INTEGER,
                   primary_key=True,
                   nullable=False,
                   unique=True,
                   autoincrement=True)
    address = db.Column(db.String(100),
                        nullable=False,
                        unique=True)
    user_id = db.Column(db.INTEGER,
                        db.ForeignKey('users.id'),
                        nullable=False)
    type = db.Column(db.TEXT,
                     nullable=False)

    data_usr = relationship('User', back_populates='my_dataobjs')

    def set(self, addr, uid, type):
        self.address = addr
        self.user_id = uid
        self.type = type

    def save(self, file=None):
        try:
            if file is not None:
                file.save(self.address)
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            if file is not None:
                try:
                    os.remove(self.address)
                except FileNotFoundError:
                    pass
                raise e

    @staticmethod
    def count():
        try:
            return db.session.query(func.count(DataObj.id)).scalar()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise e


class Algorithm(db.Model):
    __tablename__ = 'algorithms'
    id = db.Column(db.INTEGER,
                   autoincrement=True,
                   primary_key=True,
                   nullable=False,
                   unique=True)
    address = db.Column(db.String(100),
                        nullable=False,
                        unique=True)
    name = db.Column(db.TEXT,
                     nullable=False)
    description = db.Column(db.String(1000))
    creator_id = db.Column(db.INTEGER,
                           db.ForeignKey('users.id'),
                           nullable=False)
    used_time = db.Column(db.INTEGER,
                          nullable=False,
                          default=0)
    create_time = db.Column(db.TIMESTAMP,
                            nullable=False)
    input_type = db.Column(db.TEXT,
                           nullable=False)
    output_type = db.Column(db.TEXT,
                            nullable=False)
    link = db.Column(db.String(100),
                     nullable=False,
                     unique=True)

    algo_usr = relationship('User', back_populates='my_algorithms')
    used_by_queries = relationship('Query', back_populates='use_algo')

    @staticmethod
    def get_all():
        try:
            return db.session.query(Algorithm).all()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise e

    def increment(self):
        self.used_time = self.used_time + 1
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise e



class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.INTEGER,
                   primary_key=True,
                   nullable=False,
                   unique=True,
                   autoincrement=True)
    user_id = db.Column(db.INTEGER,
                        db.ForeignKey('users.id'),
                        nullable=False)
    description = db.Column(db.String(1000))
    create_time = db.Column(db.TIMESTAMP,
                            nullable=False)

    record_usr = relationship('User', back_populates='my_records')
    my_queries = relationship('Query', back_populates='in_record')

    def set(self, uid):
        self.user_id = uid,
        self.create_time = func.now()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(db.Model):
    __tablename__ = 'queries'
    id = db.Column(db.INTEGER,
                   autoincrement=True,
                   primary_key=True,
                   nullable=False,
                   unique=True)
    algo_id = db.Column(db.INTEGER,
                        db.ForeignKey('algorithms.id'),
                        nullable=False)
    record_id = db.Column(db.INTEGER,
                          db.ForeignKey('records.id'),
                          nullable=False)
    input_id = db.Column(db.INTEGER,
                         db.ForeignKey('dataobjs.id'),
                         nullable=False)
    output_id = db.Column(db.INTEGER,
                          db.ForeignKey('dataobjs.id'),
                          nullable=False)

    use_algo = relationship('Algorithm', back_populates='used_by_queries')
    in_record = relationship('Record', back_populates='my_queries')

    def set(self, rid, iid, aid, oid):
        self.algo_id = aid
        self.record_id = rid
        self.input_id = iid
        self.output_id = oid

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
