from app import app


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
#数据库
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:167258aa@127.0.0.1/flaskdb'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#mail
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '17712121935@163.com'
app.config['MAIL_PASSWORD'] = '167258aaa'

