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