DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '175689'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'platform'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"

# MAIL_USE_TLS:端口号587
# MAIL_USE_SSL:端口号465
# QQ邮箱不支持非加密方式发送邮件
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = False
MAIL_USERNAME = "1103616483@qq.com"
MAIL_PASSWORD = "qcllddsrrjqijbha"
MAIL_DEFAULT_SENDER = "1103616483@qq.com"
