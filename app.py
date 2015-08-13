from flask import Flask
from flask import render_template
from database import *
import flask
import json

def make_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

app = make_app()


@app.route('/')
def hello_world():
    print "andyafter"
    return "andyafter"

    
@app.route('/testdb')
def testdb():
    print "testdb"

@app.route('/insert')
def testinsert():
    viewer = database.User(id=1,name="andy",email="andyafter@gmail.com")
    db = session

    db.add(viewer)

    db.commit()
    
    return "success!"

@app.route('/queryById/<iden>')
def queryById(iden):
    print iden
    #r = Clinic.
    r = session.query(Clinic).filter_by(id=iden).first()
    result = {}
    print r.__dict__
    for i in r.__dict__:
        print i
        if i[0] == '_':
            continue
        else:
            result[i] = r.__dict__[i]
            
    return flask.jsonify(**result)

@app.route('/testquery')
def testQuery():

    a = session.query(User).all()
    print a[0].__dict__
    print a[0].name
    res = {}
    for i in a[0].__dict__:
        if i[0]=="_":
            continue
        res[i] = a[0].__dict__[i]
    
    """
    print a.id
    print a.name
    print a.email
    """
    return flask.jsonify(**res)
    


    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
