from flask import Flask
from flask import render_template
from flask import request
from database import *
import flask
import time
import json
from sqlalchemy import update



current_milli_time = lambda: int(round(time.time() * 1000))
def make_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

app = make_app()


@app.route('/')
def hello_world():
    print "andyafter"
    return render_template("index.html")

    
@app.route('/testdb')
def testdb():
    print "testdb"


@app.route('/testpost',methods=["POST"])
def testPost():
    data = request.form
    print data
    print "param2" in data
    return "SUCCESS"


@app.route('/insert/<iden>')
def testinsert(iden):
    viewer = User(id=iden,name="andy",email=None)
    db = session
    try:
        db.add(viewer)
    except:
        db.rollback()
        return "failed"
    db.commit()
    
    return "success!"



@app.route('/update/<iden>')
def updateById(iden):
    # this one should be post
    a = session.query(User).filter_by(id=iden).first()
    if a == None:
        return "Invalid ID!"
    a.name=u"andypan"
    session.commit()
    return "SUCCESS"


@app.route('/deleteById/<iden>')
def deleteById(iden):
    user1 = session.query(User).filter_by(id=iden).first()
    if user1 == None:
        return "no user with id " + iden
    session.delete(user1)
    session.commit()
    return "success"
    
    

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
    if len(a)==0:
        return "nothing"
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


@app.route('/queue')
def queue():
    a = session.query(Queue).filter_by(id="000000").first()
    nstr = ""

    qnum = str(int(a.key)+1)

    a.key = qnum
    nstr = qnum
    for i in range(6-len(nstr)):
        nstr = '0'+nstr
    k = str(current_milli_time())

    que = session.query(Queue).filter_by(id=nstr).first()
    if que == None:
        q = Queue(id = nstr, key = k)
        session.add(q)
    else:
        que.key = k
    session.commit()
    result = {}
    result['id'] = nstr
    result['key'] = k


    return flask.jsonify(**result)



    
@app.route('/refreshqueue')
def refresh():
    a = session.query(Queue).filter_by(id="000000").first()
    a.key = u'0'
    session.commit()
    return "success"

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
