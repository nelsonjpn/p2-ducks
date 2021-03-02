# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import Markup
import datetime
#from model import updatestats
# from flask_wtf import FlaskForm
# from wtforms import stringfield

import data  # projects definitions are placed in different file

# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, email, length

app = Flask(__name__)
dbURI = 'sqlite:///model/createDB'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
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
@app.route('/bin/', methods=["GET", "POST"])
def bin_route():
    dec = 0
    print("n bin")
    print(request.form.get("bin"))
    if request.form.get("bin") is not None and request.form.get("bin") != "":
        print(request.form.get("bin"))
        bin=request.form.get("bin")
        print('binary; ' + bin)
        dec=int(bin, 2)
        print(dec)
    return render_template("lightbulb.html", decimal=dec, projects=data.setup())


# connects /flask path of server to render example.html
@app.route('/example/', methods=["GET", "POST"])
def example_route():
    # first get the form data
    if request.form.get("txt") is not None and request.form.get("txt") != "":
        print("text: " + request.form.get("txt"))
        strTxt = request.form.get("txt")
        # now format it - the Markup import formats the HTML correctly
        example = Markup("<b><i>" + strTxt + "</i></b>")
    else:
        strTxt = ""
        example = strTxt
    # next format it
    # then return the parameter to the page
    return render_template("example.html", strTxt=strTxt, example=example, projects=data.setup())


# connects to /easteregg/
@app.route('/easteregg/')
def easteregg_route():
    return render_template('easteregg.html')


class SiteStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.VARCHAR)
    datevisit = db.Column(db.VARCHAR)


def update_stats(site):
    try:
        dt = datetime.datetime.now()
        v1 = SiteStats(sitename=site, datevisit=str(dt))
        print("Variable: " + v1.sitename + " " + v1.datevisit)
        print("database:" + app.config['SQLALCHEMY_DATABASE_URI'])
        db.session.add(v1)
        db.session.commit()
    finally:
        print("Done")



# connects /flask path of server to render Char_codes.html
@app.route('/char/', methods=["GET","POST"])
def char_route():
    # get value sent by form, and format them
    print("Ascii" + str(request.form.get("ASCIICode")))
    # first the ascii code
    if request.form.get("ASCIICode") is not None:
        strAscii = Markup("&#" + request.form.get("ASCIICode") + ";")
    else:
        strAscii = ""
    # second the unicode code
    if request.form.get("UnicodeCode") is not None:
        strUnicode = Markup("&#" + request.form.get("UnicodeCode") + ";")
    else:
        strUnicode = ""
    # return the page, sending ASCII and Unicode parameters
    return render_template("char_codes.html", asciicode=strAscii, unicode=strUnicode, projects=data.setup())


# connects /flask path of server to render rgb.html
@app.route('/rgb/', methods=["GET", "POST"])
def rgb_route():
    codeRed=255
    codeGreen=255
    codeBlue=255
    if request.form.get("codeRed") is not None:
        codeRed=request.form.get("codeRed")
    if request.form.get("codeGreen") is not None:
        codeGreen=request.form.get("codeGreen")
    if request.form.get("codeBlue") is not None:
        codeBlue=request.form.get("codeBlue")
    # update the count for rgb
    update_stats("rgb")
    return render_template("rgb.html", red=codeRed, green=codeGreen, blue=codeBlue, projects=data.setup())


# connects /flask path of server to render gif.html
@app.route('/gif/'), methods=["GET", "POST"])
def gif_route():
    giftype="charm"
    if request.form.get("charm") is not None:
        charm=request.form.get("charm")
    if request.form.get("bulb") is not None:
        bulb=request.form.get("bulb")
    if request.form.get("pika") is not None:
        pika=request.form.get("pika")
    if request.form.get("squirt") is not None:
        squirt=request.form.get("squirt")
    update_stats("giftype")
    return render_template("gif.html", ch=charm, pi=pika, sq=squirt, bu=bulb, projects=data.setup())

@app.route("/project/runtime")
def runtime_route():
    return render_template("task.html", data=data.runtime())


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
