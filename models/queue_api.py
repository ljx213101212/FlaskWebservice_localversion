__author__ = 'andypan'
# here I pack all the operation of the queue related api
import time
import random
from database import *

# if you want to query the max id number for new creations
# a =  session.query(func.max(Clinic.id)).all()

current_milli_time = lambda: int(round(time.time() * 1000))

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

def generate_queue(clinic_name, uuid):
    # assume that hospital name does not repeat
    clinic = session.query(Clinic).filter_by(name=clinic_name).first()
    if not clinic:
        return "Clinic name does not exist!"
    k = str(current_milli_time())
    docs = clinic.doctors
    docindex = random.randrange(0, len(docs))
    rows = session.query(Queue).count()
    cur_queue = docs[docindex].current_queue_num
    queue_num = str(cur_queue+1)

    # 3 digits of queue number
    while len(queue_num) < 3:
        queue_num = '0'+queue_num

    # doctor number in the hospital
    queue_num=str(docindex)+queue_num
    # another 3 digits of doctor number
    while len(queue_num) < 6:
        queue_num = '0'+queue_num

    queue = Queue(id=rows+1, key=k, uuid=uuid)
    queue.queue_number = queue_num
    # this one I add one to start from 1
    docs[docindex].queue_id.append(queue)
    if not docs[docindex].current_queue_num:
        docs[docindex].current_queue_num = 1
    else:
        docs[docindex].current_queue_num +=1
    session.add(queue)
    session.commit()
    result = {}
    result["queue_num"] = queue_num
    result["key"] = k
    result["doctor"] = docs[docindex].name
    return result


#result['error'] = j0  ---  No doctor available
#result['error'] = j1  ---  Patient need to register first

def generate_queue_li(clinic_name, uuid, ic_no):
    result = {}

    #print "1231231231"
    #print clinic_name,uuid,ic_no
    # assume that hospital name does not repeat
    clinic = session.query(Clinic).filter_by(name=clinic_name).first()
    if not clinic:
        result['error'] = "Clinic name does not exist!"
    
    k = str(current_milli_time())

    clinic_id = clinic.id

    print clinic_id

    queue_num = session.query(Queue).filter_by(clinic_id=clinic_id).count()
    print queue_num
    doctor = session.query(Doctor).filter_by(clinic_id=clinic_id).first()

    if not doctor:
        result['error'] = "j0"
        print "No doctor available!"
        return result
    else:
        doctor = session.query(Doctor).filter_by(clinic_id=clinic_id,flag=0).first()
        if not doctor:
            reset_flag()
            doctor = session.query(Doctor).filter_by(clinic_id=clinic_id,flag=0).first()

    patient_detail = session.query(PatientDetail).filter_by(ic_num=ic_no).first()
    patient = None
    if patient_detail:
        patient = session.query(Patient).filter_by(patient_id=patient_detail.patient_id).first()

    # if not patient_detail:
    #     result['error'] = "j1"
    #     print "You need register first"
    #     return result
    # patient = session.query(Patient).filter_by(patient_id=patient_detail.patient_id).first()

    # if not patient:
    #     result['error'] = "j1"
    #     print result
    #     return result

    print queue_num
    print doctor.name
    #print patient.patient_id

    queue = Queue(key=k, uuid=uuid,clinic_id=clinic_id)
    queue.queue_number = queue_num + 1
    queue.doctor_id = doctor.id
    if patient:
        queue.patient_id = patient.patient_id
    doctor.current_queue_num = queue_num + 1
    set_flag(doctor)


    session.add(queue)
    session.add(doctor)
    session.commit()

   
    result["queue_num"] = queue_num + 1
    result["key"] = k
    result["doctor"] = doctor.name
    return result

    # queue.queue_number = queue_num
    # # this one I add one to start from 1
    # docs[docindex].queue_id.append(queue)
    # if not docs[docindex].current_queue_num:
    #     docs[docindex].current_queue_num = 1
    # else:
    #     docs[docindex].current_queue_num +=1
    # session.add(queue)
    # session.commit()
    # result = {}
    # result["queue_num"] = queue_num
    # result["key"] = k
    # result["doctor"] = docs[docindex].name
    # return result


# clinic_name="RIDGEWOOD MEDICAL CLINIC"
# uuid="b1d1b0131e"
# ic_no = "t"

# print generate_queue(clinic_name,uuid,ic_no)


def reset_flag():
    doctors = session.query(Doctor).order_by(Doctor.id.desc())
    for doctor in doctors:
        doctor.flag = 0
    session.commit()

def set_flag(doctor):
    doctor.flag = 1


