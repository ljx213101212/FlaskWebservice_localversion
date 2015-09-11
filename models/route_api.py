__author__='jx'
from geopy.distance import great_circle

def isWithNKilometers(src_lat,src_lng,kilo,lat,lng):
    newport_ri = (src_lat,src_lng)
    cleveland_oh = (lat,lng)
    #print "&&&&&&&&&"
    #print kilo
    distance = great_circle(newport_ri, cleveland_oh).kilometers
    #print distance
    if distance >= float(kilo):
        return False
    else:
        print "&&&&&&&&&"
        print distance
        return True


src_lat=41.49008
src_lng=-71.312796

lat=41.499498
lng=-81.695391

kilo=3000

print isWithNKilometers(src_lat,src_lng,kilo,lat,lng)

