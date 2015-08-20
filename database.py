from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
import sqlite3


Base = declarative_base()
#Base.metadata.create_all(bine=engine)

engine = create_engine(config.DATABASEURI)
metadata = MetaData(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


class Queue(Base):
    __tablename__ = 'queue'
    id = Column(String(10), primary_key=True) # maximum 10,
    key = Column(String(50))

    def __init__(self, id,key=None):
        self.id = id
        self.key = key

    def __repr__(self):
        return '<Queue Number %r>' % (self.id)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))

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
    public_holiday = Column(String(256))
    remarks =  Column(String(256))


    def __init__(self, id,name=None, aviva_code=None,\
                 zone=None, estate=None,address1=None,address2=None,\
                 postal=None,telephone=None,fax=None,weekday=None,\
                 saturday=None,sunday=None,public_holiday=None,remarks=None):
        self.id = id
        self.name = name
        self.aviva_code = aviva_code
        self.zone = zone
        self.estate = estate
        self.address1 = address1
        self.address2 = address2
        self.postal = postal
        self.telephone = telephone
        self.fax = fax
        self.weekday = weekday
        self.saturday = saturday
        self.sunday = sunday
        self.public_holiday = public_holiday
        self.remarks = remarks
        
    def __repr__(self):
        return '<Clinic %r>' % (self.name)
    


def connect_db(app):
    print "connect_db: %s" % app.config['DATABASE']
    db = sqlite3.connect(app.config['DATABASE'])
    db.cursor().executescript("PRAGMA foreign_keys = ON;") # should implement delete-cascade but doesn't
    return db
    
