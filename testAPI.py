import math

nodes = [
    {
        "longitude": 44.457,
        "latitude": 26.093,
        "name": "Bucharest"
    },
    {
        "longitude": 46.181,
        "latitude": 21.312,
        "name": "Arad"
    },
    {
        "longitude": 46.624,
        "latitude": 21.518,
        "name": "Zerind"
    },
    {
        "longitude": 47.089,
        "latitude": 21.907,
        "name": "Oradea"
    },
    {
        "longitude": 45.794,
        "latitude": 24.128,
        "name": "Sibiu"
    },
    {
        "longitude": 45.842,
        "latitude": 24.973,
        "name": "Fagaras"
    },
    {
        "longitude": 45.756,
        "latitude": 21.231,
        "name": "Timisoara"
    },
    {
        "longitude": 45.691,
        "latitude": 21.903,
        "name": "Lugoj"
    },
    {
        "longitude": 44.904,
        "latitude": 22.365,
        "name": "Mehadia"
    },
    {
        "longitude": 44.639,
        "latitude": 22.659,
        "name": "Drobeta"
    },
    {
        "longitude": 44.319,
        "latitude": 23.794,
        "name": "Cralova"
    },
    {
        "longitude": 45.099,
        "latitude": 24.369,
        "name": "Rimnicu Vilcea"
    },
    {
        "longitude": 44.856,
        "latitude": 24.869,
        "name": "Pitesti"
    },
    {
        "longitude": 43.905,
        "latitude": 25.969,
        "name": "Giurgiu"
    },
    {
        "longitude": 44.718,
        "latitude": 26.645,
        "name": "Urziceni"
    },
    {
        "longitude": 47.056,
        "latitude": 26.506,
        "name": "Neamt"
    },
    {
        "longitude": 47.158,
        "latitude": 27.598,
        "name": "Iasi"
    },
    {
        "longitude": 46.641,
        "latitude": 27.728,
        "name": "Vaslui"
    },
    {
        "longitude": 44.69,
        "latitude": 27.945,
        "name": "Hirsova"
    },
    {
        "longitude": 44.049,
        "latitude": 28.653,
        "name": "Eforie"
    }
]

adj = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Bucharest
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Arad
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Zering
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Oradea
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def getIndexCity(city, nodes, adj):
    index = 0
    for i in nodes:
        if (i["name"] == city):
            return index
        index += 1


def getAdj(city, nodes, adj):
    indexCity = getIndexCity(city, nodes, adj)
    indexAdj = 0
    arrayAdj = []
    for i in adj[indexCity]:
        if (i == 1):
            # arrayAdj.append(nodes[indexAdj]["name"])
            arrayAdj.append(nodes[indexAdj])
        indexAdj += 1
    return arrayAdj


def getDistance(lng1, lat1, lng2, lat2):
    distLon = (lng2 - lng1) * math.pi / 180.0
    distLat = (lat2 - lat1) * math.pi / 180.0
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    a = ((((math.sin(distLon/2))**2) *
         math.cos(lat1) * math.cos(lat2)) + (math.sin(distLat/2)**2))
    c = 2 * math.asin(math.sqrt(a))
    dist = c * 6371
    return dist


def getDistanceBetweenCity(nodeKotaAwal, nodeKotaTujuan):
    distance = getDistance(
        nodeKotaAwal["longitude"], nodeKotaAwal["latitude"], nodeKotaTujuan["longitude"], nodeKotaTujuan["latitude"])
    return distance


# cityNode = node kota awal ke tetangga
def getDistanceBetweenAllCity(cityNode, nodes, adj):
    adjCity = getAdj(cityNode["name"], nodes, adj)
    for node in adjCity:
        node["distance"] = getDistance(
            cityNode["longitude"], cityNode["latitude"], node["longitude"], node["latitude"])
    return adjCity


# cityNode = node kota tujuan, h(n)
def getDistanceToCity(cityNode, nodes, adj):
    greedySearch = []
    for node in nodes:
        greedySearch.append(getDistance(
            cityNode["longitude"], cityNode["latitude"], node["longitude"], node["latitude"]))
    return greedySearch


# minimum distance format input [x, [y,y,y,y]]; x nilai, y rute
def getIndexMinimumDistance(arrayRute):
    minimum = arrayRute[0]
    index = 0
    for i in range(len(arrayRute)):
        if ((minimum[0]) > (arrayRute[i][0])):
            minimum = arrayRute[i]
            index = i
    return index


def getMinimum(arrayRute):
    for i in arrayRute:
        if (i != 0):
            minimum = i
            break
    for i in range(len(arrayRute)):
        minimum = arrayRute[i]
    return minimum


# belom beres
def aStarPath(kotaAwal, kotaTujuan, nodes, adj):
    indexKotaAwal = getIndexCity(kotaAwal, nodes, adj)
    indexKotaTujuan = getIndexCity(kotaTujuan, nodes, adj)
    uniformSearch = adj

    # g(n)
    for i in range(len(uniformSearch)):
        for j in range(len(uniformSearch)):
            if (uniformSearch[i][j] != 0):
                uniformSearch[i][j] = getDistanceBetweenCity(
                    nodes[i], nodes[j])
    print(uniformSearch)
    print("")
    # h(n)
    greedySearch = getDistanceToCity(nodes[indexKotaTujuan], nodes, adj)
    print(greedySearch)

    # f(n)


aStarPath("Arad", "Bucharest", nodes, adj)
