# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import Markup
# from model import site_stats
# from model import db
import datetime
# from flask_wtf import FlaskForm
# from wtforms import stringfield

import data  # projects definitions are placed in different file

# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, email, length

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///model/createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI

db = SQLAlchemy(app)


# connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("p2-ducks.html", projects=data.setup())


# connects /hello path of server to render p2-ducks.html
@app.route('/ducks/')
def ducks_route():
    return render_template("p2-ducks.html", projects=data.setup())


# connects /flask path of server to render lightbulb.html
@app.route('/bin/', methods=["GET", "POST"])
def bin_route():
    # first get the form data
    dec = 0
    if request.form.get("bin") is not None and request.form.get("bin") != "":
        print(request.form.get("bin"))
        b = request.form.get("bin")
        dec = int(b, 2)
    update_stats('bin')
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
    # log visit
    update_stats('example')
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

    update_stats('char')
    # return the page, sending ASCII and Unicode parameters
    return render_template("char_codes.html", asciicode=strAscii, unicode=strUnicode, projects=data.setup())


# connects /flask path of server to render rgb.html
@app.route('/rgb/')
def rgb_route():
    # update the count for rgb\
    return render_template("rgb.html", projects=data.setup())


# connects /flask path of server to render gif.html
@app.route('/gif/')
def gif_route():
    # update the count for gif
    return render_template("gif.html", projects=data.setup())


@app.route("/project/runtime")
def runtime_route():
    return render_template("task.html", data=data.runtime())


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
