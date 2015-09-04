import os, sys
import time
lib_path = os.path.abspath(os.path.join('..', '..', '..', 'www','DocHeroku2'))
sys.path.append(lib_path)

from database import *


##test

current_milli_time = lambda: int(round(time.time() * 1000))

def generate_queue_li(clinic_name, uuid, ic_no):
    result = {}

    print "1231231231"
    #print clinic_name,uuid,ic_no
    # assume that hospital name does not repeat
    clinic = session.query(Clinic).filter_by(name=clinic_name).first()
    if not clinic:
        result['error'] = "Clinic name does not exist!"
    
    k = str(current_milli_time())

    clinic_id = clinic.id

    print clinic_id

    # queue_num = session.query(Queue).filter_by(clinic_id=clinic_id).count()
    # doctor = session.query(Doctor).filter_by(clinic_id=clinic_id,current_queue_num=None).first()

    # if not doctor:
    #     result['error'] = "No doctor available!"
    #     print "No doctor available!"
    # patient_detail = session.query(PatientDetail).filter_by(ic_num=ic_no).first()

    # if not patient_detail:
    #     result['error'] = "Please register with the clinic1!"
    # patient = session.query(Patient).filter_by(patient_id=patient_detail.patient_id).first()

    # if not patient:
    #     result['error'] = "Please register with the clinic2!"
    # print queue_num
    # print doctor.name
    # print patient.patient_id

    # queue = Queue(key=k, uuid=uuid)
    # queue.queue_number = queue_num + 1
    # queue.doctor_id = doctor.id
    # queue.patient_id = patient.patient_id
    # doctor.current_queue_num = queue_num + 1


    # session.add(queue)
    # session.add(doctor)
    # session.commit()

   
    # result["queue_num"] = queue_num + 1
    # result["key"] = k
    # result["doctor"] = doctor.name
    #return result

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
