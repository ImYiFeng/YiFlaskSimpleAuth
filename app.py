from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.secret_key = '0'

#   https://www.runoob.com/python3/python-with.html
with open('config.json') as config_file:
    config = json.load(config_file)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config['USERNAME']}:{config['PASSWORD']}@{config['HOSTNAME']}:{config['PORT']}/{config['DATABASE']}?charset=utf8mb4"

#   ORM模型
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    userlogin = User.query.filter_by(username=username).first()
    if userlogin and userlogin.password == password:
        if userlogin.username == "admin":
            session['is_admin'] = True  #会话
            return redirect('/admin')
        return '登录成功'
    else:
        return '账号或密码错误'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        userexist = User.query.filter_by(username=username).first()
        if userexist:
            return '用户名已存在'
        elif password1 != password2:
            return '前后密码不一致'
        else:
            user = User(username=username, password=password1)
            db.session.add(user)
            db.session.commit()
            return '注册成功'


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('is_admin'):
        return redirect('/')
    usermanage = User.query.all()
    return render_template("admin.html", users=usermanage)


@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if not session.get('is_admin'):
        return redirect('/')
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect('/admin')


@app.route('/change_password/<int:user_id>', methods=['POST'])
def change_password(user_id):
    if not session.get('is_admin'):
        return redirect('/')
    new_password = request.form['new_password']
    user = User.query.get(user_id)
    if user:
        user.password = new_password
        db.session.commit()
    return redirect('/admin')


if __name__ == '__main__':
    app.run()
