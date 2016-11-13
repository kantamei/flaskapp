from app import app


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:167258aa@127.0.0.1/flaskdb'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True