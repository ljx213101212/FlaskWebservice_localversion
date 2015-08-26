__author__ = 'andypan'
# here I pack all the operation of the queue related api

from database import *

# if you want to query the max id number for new creations
# a =  session.query(func.max(Clinic.id)).all()

def testmodel():
    a = session.query(Clinic).filter_by(id=1).first()
    return a.name

def refresh_queue_by_clinic_id(iden):
    # here I played dirty by making the record with
    clinic = session.query(Clinic).filter_by(id=iden).first()
    for doc in clinic.doctors:
        print doc.name
        print doc.current_queue_num
        doc.current_queue_num = 0
        print doc.current_queue_num
    session.commit()
    return "success"