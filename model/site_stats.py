from flask import Flask
import datetime
from model import db

app = Flask(__name__)


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