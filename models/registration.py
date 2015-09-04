__author__ = 'andypan'

from database import *

def register(name, ic_num, queue_num, phone_num=None):
    # this part is dirty cause there is 2 and more database
    # operations
    q = session.query(Queue).filter_by(queue_num=queue_num).first()
    doc = session.query(Doctor).filter_by(id=q.doctor_id).first()
    clinic = session.query(Clinic).filter_by(doc.clinic_id).first()

    count = session.query(Patient).count()
    patient = Patient(patient_id=count+1, name = name)
    patient.queue.append(q)

    ## about patient detail
    dcount = session.query(PatientDetail).count()
    patient_detail = PatientDetail(id=dcount+1,ic_num=ic_num)
    if phone_num:
        patient_detail.phone_num = phone_num

    ## adding the foreign key reference
    clinic.patient_detail.append(patient_detail)
    patient.detail.append(patient_detail)
    ## end of adding foreign key reference
    session.add(patient_detail)
    session.add(patient)
    session.commit()

    return "success"


#return:
#0---  ic_num duplicated
#1---  process succeed
def register_li(patient_name,clinic_name, ic_num, phone_num=None):
    # this part is dirty cause there is 2 and more database
    # operations
    # q = session.query(Queue).filter_by(queue_num=queue_num).first()
    # doc = session.query(Doctor).filter_by(id=q.doctor_id).first()
    clinic = session.query(Clinic).filter_by(name=clinic_name).first()
    clinic_id = clinic.id 

    # count = session.query(Patient).count()
    # patient = Patient(patient_id=count+1, name = name)
    # patient.queue.append(q)

    ## about patient detail
    # dcount = session.query(PatientDetail).count()

    patient = Patient(name=patient_name)
    session.add(patient)
    session.commit()

    #patient = session.query(Patient).filter_by(name=patient_name).first()
    patient_id = patient.patient_id
    print patient_id

    if isIc_NumDuplicated(ic_num):
        print "ic_num duplicated"
        return '0'


    patient_detail = PatientDetail(patient_id=patient_id,ic_num=ic_num,phone_num=phone_num)


    if phone_num:
        patient_detail.phone_num = phone_num

    ## end of adding foreign key reference
    session.add(patient_detail)
    session.commit()

    print "success"
    return '1'


def isIc_NumDuplicated(ic_num):
    patient_detail = session.query(PatientDetail).filter_by(ic_num=ic_num).first()
    if patient_detail:
        return True
    else:
        return False
