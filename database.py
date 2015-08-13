from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
import sqlite3


Base = declarative_base()

engine = create_engine(config.DATABASEURI)
metadata = MetaData(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, id,name=None, email=None):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class Clinic(Base):
    __tablename__ = 'clinic'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    aviva_code =  Column(String(32))
    zone =  Column(String(64))
    estate =  Column(String(64))
    address1 =  Column(String(256))
    address2 =  Column(String(256))
    postal =  Column(String(32))
    telephone =  Column(String(64))
    fax =  Column(String(64))

    # for operating hours I just stored them as strings
    # you guys figure it out
    weekday =  Column(String(256))
    saturday =  Column(String(256))
    sunday =  Column(String(256))
    remarks =  Column(String(256))


    def __init__(self, id,name=None, aviva_code=None,\
                 ):
        self.id = id
        self.name = name
        self.aviva_code = aviva_code
    


def connect_db(app):
    print "connect_db: %s" % app.config['DATABASE']
    db = sqlite3.connect(app.config['DATABASE'])
    db.cursor().executescript("PRAGMA foreign_keys = ON;") # should implement delete-cascade but doesn't
    return db
    
