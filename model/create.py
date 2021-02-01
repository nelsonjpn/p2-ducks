from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import datetime

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
dt = datetime.datetime.now()

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class SiteStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.VARCHAR)
    datevisit = db.Column(db.VARCHAR)

if __name__ == "__main__":
    """create each table"""
    db.create_all()
    try:
        v1 = SiteStats(sitename='char', datevisit=str(dt))
        session.add_all([v1])
        session.commit()
    except:
        print("Records exist")

    print("Table: Visits")
    list = SiteStats.query.all()
    for row in list:
        print("Visits: " + row.sitename + ", Date: " + row.datevisit)

"""
Test on Terminal from IntelliJ
sqlite> .open createDB
sqlite> .tables
SiteStats
"""
