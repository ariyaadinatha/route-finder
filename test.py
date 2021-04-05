import math

# format coor (lon,lat)
# Menggunakan formula haversine


def getDistance(coor1, coor2):
    distLon = (coor2[0] - coor1[0]) * math.pi / 180.0
    distLat = (coor2[1] - coor1[1]) * math.pi / 180.0
    coor1[1] = (coor1[1]) * math.pi / 180.0
    coor2[1] = (coor2[1]) * math.pi / 180.0

    a = ((((math.sin(distLon/2))**2) *
         math.cos(coor1[1]) * math.cos(coor2[1])) + (math.sin(distLat/2)**2))
    c = 2 * math.asin(math.sqrt(a))
    dist = c * 6371
    return dist


coor1 = [107.60969191789626, -6.8896571064314855]
coor2 = [107.61146217584607, -6.890908639963897]

print(getDistance(coor1, coor2))
