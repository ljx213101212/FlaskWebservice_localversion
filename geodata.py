from database import *
import json
from pprint import pprint

cdat = open('./data/Clinic.json','r')

data = json.loads(cdat.read())
print data.items()[0][1][1]  # this is one of the objects
print data.items()[0][1][1][u'ADDRESS_1']



cdat.close