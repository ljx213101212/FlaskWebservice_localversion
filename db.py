from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  config.DATABASEURI
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    #email = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name
        #self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    #aviva_code = db.Column(db.String(32), unique=True)
    #zone = db.Column(db.String(64), unique=True)
    #estate = db.Column(db.String(64), unique=True)
    #address1 = db.Column(db.String(256), unique=True)
    #address2 = db.Column(db.String(256), unique=True)
    #postal = db.Column(db.String(32), unique=True)
    #telephone =  db.Column(db.String(32), unique=True)
    
    #email = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name
        #self.email = email

    def __repr__(self):
        return '<Clinic %r>' % self.name



def connect_db(app):

    print "Connect to Database: %s" % app.config['DATABASE']
    db = sqlite3.connect(app.config['DATABASE'])
    db.cursor().executescript("PRAGMA foreign_keys = ON;") # should implement delete-cascade but doesn't
    return db
