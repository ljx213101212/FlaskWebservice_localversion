from database import *
import json

'''
location
zone
estate
fax_no
objectid
sunday
longitude
telephone
sn
clinic
monday_friday
public_holiday
address_1
address_2
updatedat
latitude
postal
saturday
createdat
aviva_code

(address1=None,address2=None,aviva_code=None,\
                 clinic=None,estate=None, fax_no=None, \
                 monday_friday=None,postal=None,public_holiday=None,remarks=None,\
                 saturday=None,sn=None,sunday=None,telephone=None,\
                 zone=None,create_at=None,update_at=None,acl=None,latitude=None,\
                 longtitude=None):

u'LONGITUDE'
u'LATITUDE'


'''

cdat = open('./data/Clinic.json','r')

data = json.loads(cdat.read())
print data.items()[0][1][1]  # this is one of the objects


for i in data.items()[0][1]:
    id = i["SN"]
    lat = i['LATITUDE']
    lng = i['LONGITUDE']
    a = session.query(DClinic).filter_by(id=id).first()
    if not a:
        d = DClinic(id = id,latitude=lat,longitude=lng)
        print d
        session.add(d)
        session.commit()
    else :
        a.latitude = lat
        a.longitude = lng
        session.commit()



cdat.close()