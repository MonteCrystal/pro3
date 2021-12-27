from flask import current_app
from flask_httpauth import HTTPBasicAuth
from flask_login import UserMixin
from server.app.init import db
from sqlalchemy.orm import relationship
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER,
                   autoincrement=True,
                   primary_key=True,
                   nullable=False)
    user_name = db.Column(db.String(30),
                          nullable=False)
    age = db.Column(db.String(3))
    password = db.Column(db.String(500))
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(50),
                      nullable=False,
                      unique=True)

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
