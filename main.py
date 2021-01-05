# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import stringfield

import data  # projects definitions are placed in different file

# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, email, length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Program Files (x86)\\SQLITE\\myDB.db'
Bootstrap(app)
db = SQLAlchemy(app)

# class LoginForm(FlaskForm):


class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# create a Flask instance
# app = Flask(__name__)


# connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("p2-ducks.html", projects=data.setup())

# connects /hello path of server to render hello.html
@app.route('/PaulN/')
def hello_route():
    print('In PaulN')
    user = Users.query.filter_by(UserID=1).first()
    print(user.username)
    return render_template("PaulN.html", projects=data.setup())


# connects /hello path of server to render p2-ducks.html
@app.route('/ducks/')
def ducks_route():
    return render_template("p2-ducks.html", projects=data.setup())


# connects /flask path of server to render binary.html
@app.route('/bin/')
def bin_route():
    return render_template("binary.html", projects=data.setup())


# connects /flask path of server to render Char_codes.html
@app.route('/char/')
def char_route():
    return render_template("char_codes.html", projects=data.setup())


# connects /flask path of server to render rgb.html
@app.route('/rgb/')
def rgb_route():
    return render_template("rgb.html", projects=data.setup())


# connects /flask path of server to render gif.html
@app.route('/gif/')
def gif_route():
    return render_template("gif.html", projects=data.setup())


@app.route("/project/runtime")
def runtime_route():
    return render_template("task.html", data=data.runtime())





if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
