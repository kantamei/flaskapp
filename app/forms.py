from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, email
from app import login_manager
from .models import User

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), email()])
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('注册')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))