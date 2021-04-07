import math

# nodes = [
#     {
#         "longitude": 44.457,
#         "latitude": 26.093,
#         "name": "Bucharest"
#     },
#     {
#         "longitude": 46.181,
#         "latitude": 21.312,
#         "name": "Arad"
#     },
#     {
#         "longitude": 46.624,
#         "latitude": 21.518,
#         "name": "Zerind"
#     },
#     {
#         "longitude": 47.089,
#         "latitude": 21.907,
#         "name": "Oradea"
#     },
#     {
#         "longitude": 45.794,
#         "latitude": 24.128,
#         "name": "Sibiu"
#     },
#     {
#         "longitude": 45.842,
#         "latitude": 24.973,
#         "name": "Fagaras"
#     },
#     {
#         "longitude": 45.756,
#         "latitude": 21.231,
#         "name": "Timisoara"
#     },
#     {
#         "longitude": 45.691,
#         "latitude": 21.903,
#         "name": "Lugoj"
#     },
#     {
#         "longitude": 44.904,
#         "latitude": 22.365,
#         "name": "Mehadia"
#     },
#     {
#         "longitude": 44.639,
#         "latitude": 22.659,
#         "name": "Drobeta"
#     },
#     {
#         "longitude": 44.319,
#         "latitude": 23.794,
#         "name": "Cralova"
#     },
#     {
#         "longitude": 45.099,
#         "latitude": 24.369,
#         "name": "Rimnicu Vilcea"
#     },
#     {
#         "longitude": 44.856,
#         "latitude": 24.869,
#         "name": "Pitesti"
#     },
#     {
#         "longitude": 43.905,
#         "latitude": 25.969,
#         "name": "Giurgiu"
#     },
#     {
#         "longitude": 44.718,
#         "latitude": 26.645,
#         "name": "Urziceni"
#     },
#     {
#         "longitude": 47.056,
#         "latitude": 26.506,
#         "name": "Neamt"
#     },
#     {
#         "longitude": 47.158,
#         "latitude": 27.598,
#         "name": "Iasi"
#     },
#     {
#         "longitude": 46.641,
#         "latitude": 27.728,
#         "name": "Vaslui"
#     },
#     {
#         "longitude": 44.69,
#         "latitude": 27.945,
#         "name": "Hirsova"
#     },
#     {
#         "longitude": 44.049,
#         "latitude": 28.653,
#         "name": "Eforie"
#     }
# ]

# adj = [
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Bucharest
#     [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Arad
#     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Zering
#     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Oradea
#     [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]


nodes = [
    {
        "longitude": 0,
        "latitude": 10,
        "name": "A"
    },
    {
        "longitude": 0,
        "latitude": 0,
        "name": "B"
    },
    {
        "longitude": 5,
        "latitude": 0,
        "name": "C"
    },
    {
        "longitude": 5,
        "latitude": 5,
        "name": "D"
    }

]

adj = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
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
        if (i != 0):
            # arrayAdj.append(nodes[indexAdj]["name"])
            arrayAdj.append(nodes[indexAdj])
        indexAdj += 1
    return arrayAdj


def getAdjIndex(city, nodes, adj):
    indexCity = getIndexCity(city, nodes, adj)
    indexAdj = 0
    arrayAdj = []
    for i in adj[indexCity]:
        if (i != 0):
            # arrayAdj.append(nodes[indexAdj]["name"])
            arrayAdj.append(indexAdj)
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

def getProcessMinimumFn(nodeProcessArray):
    minProcess = min(nodeProcessArray, key = lambda el: el["fn"])

    return minProcess



def getMinimum(arrayRute):
    for i in arrayRute:
        if (i != 0):
            minimum = i
            break
    for i in range(len(arrayRute)):
        minimum = arrayRute[i]
    return minimum

def hn(kotaAwal, kotaTujuan):
    return getDistanceBetweenCity(kotaAwal, kotaTujuan)

def gn(nodeProcessAwal, kotaNext, nodes):
    nameKotaAwal = nodeProcessAwal["node"]["name"]
    indexKotaAwal = getIndexCity(nameKotaAwal, nodes, adj)
    nodeKotaAwal = nodes[indexKotaAwal]

    indexkotaNext = getIndexCity(kotaNext, nodes, adj)
    nodekotaNext = nodes[indexkotaNext]

    return getDistanceBetweenCity(nodeKotaAwal, nodekotaNext) + nodeProcessAwal["gn"]



def fn(nodeProcessAwal, kotaNext, kotaTujuan, nodes, adj):
    # list node yg sudah dikunjungi
    # fn
    # node itu sendiri
    #
    #
    indexKotaTujuan = getIndexCity(kotaTujuan, nodes, adj)
    nodeKotaTujuan = nodes[indexKotaTujuan]

    nodeProcessNext = {}

    indexkotaNext = getIndexCity(kotaNext, nodes, adj)
    nodekotaNext = nodes[indexkotaNext]
    nodeProcessNext["node"] = nodekotaNext


    nameKotaAwal = nodeProcessAwal["node"]["name"]
    indexKotaAwal = getIndexCity(nameKotaAwal, nodes, adj)
    nodeProcessNext["visited"] = [indexKotaVisited for indexKotaVisited in nodeProcessAwal["visited"]]
    nodeProcessNext["visited"].append(indexKotaAwal)

    f = 0

    h = hn(nodekotaNext, nodeKotaTujuan)
    nodeProcessNext["hn"] = h
    f += h

    g = gn(nodeProcessAwal, kotaNext, nodes)
    nodeProcessNext["gn"] = g
    f += g

    nodeProcessNext["fn"] = f


    return nodeProcessNext



# nodeProcessAwal = {
#     "node": nodes[0],
#     "visited": [1, 2, 3],
#     "gn" : 100
# }

# print(fn(nodeProcessAwal, "D", "B", nodes, adj))

# print(getAdjIndex("C", nodes, adj))
# print(getAdjIndex("D", nodes, adj))

def isPathAvailable(kotaAwal, kotaTujuan, nodes, adj):
    indexKotaAwal = getIndexCity(kotaAwal, nodes, adj)
    indexKotaTujuan = getIndexCity(kotaTujuan, nodes, adj)

    kotaVisited = [False for node in nodes]
    nextKotaVisitTargetIndex = []

    kotaCurrent = kotaAwal
    indexKotaCurrent = getIndexCity(kotaCurrent, nodes, adj)
    nodeKotaCurrent = nodes[indexKotaCurrent]

    tetangga = getAdjIndex(kotaCurrent, nodes, adj)

    for indexTetangga in tetangga:
        if (not(kotaVisited[indexTetangga])):
            kotaVisited[indexTetangga] = True
            nextKotaVisitTargetIndex.append(indexTetangga)

    while (kotaCurrent != kotaTujuan and len(nextKotaVisitTargetIndex) != 0):

        # re assign kota current
        indexKotaCurrent = nextKotaVisitTargetIndex[0]
        nodeKotaCurrent = nodes[indexKotaCurrent]
        kotaCurrent = nodeKotaCurrent["name"]
        
        del nextKotaVisitTargetIndex[0]

        tetangga = getAdjIndex(kotaCurrent, nodes, adj)

        for indexTetangga in tetangga:
            if (not(kotaVisited[indexTetangga])):
                kotaVisited[indexTetangga] = True
                nextKotaVisitTargetIndex.append(indexTetangga)
    
    return kotaCurrent == kotaTujuan


# belom beres
def aStarPath(kotaAwal, kotaTujuan, nodes, adj):
    if (isPathAvailable(kotaAwal, kotaTujuan, nodes, adj)):
        indexKotaAwal = getIndexCity(kotaAwal, nodes, adj)
        indexKotaTujuan = getIndexCity(kotaTujuan, nodes, adj)

        nextNodesProcess = []

        kotaCurrent = kotaAwal
        indexKotaCurrent = getIndexCity(kotaCurrent, nodes, adj)
        nodeKotaCurrent = nodes[indexKotaCurrent]
        nodeProcessCurrent = {
            "node": nodeKotaCurrent,
            "gn": 0,
            "visited": [] 
        }

        while (kotaCurrent != kotaTujuan):
            tetangga = getAdjIndex(kotaCurrent, nodes, adj)

            for indexTetangga in tetangga:
                nodeTetangga = nodes[indexTetangga]
                kotaTetangga = nodeTetangga["name"]

                # fn
                nodeTetanggaProcess = fn(nodeProcessCurrent, kotaTetangga, kotaTujuan, nodes, adj)
                nextNodesProcess.append(nodeTetanggaProcess)

            # get the minimum value of fn
            minProcess = getProcessMinimumFn(nextNodesProcess)
            indexMinProcess = nextNodesProcess.index(minProcess)
            del nextNodesProcess[indexMinProcess]

            # reassign kota current state
            kotaCurrent = minProcess["node"]["name"]
            indexKotaCurrent = getIndexCity(kotaCurrent, nodes, adj)
            nodeKotaCurrent = nodes[indexKotaCurrent]
            nodeProcessCurrent = minProcess

        nodeProcessCurrent["error"] = False

        return nodeProcessCurrent
    else :
        return {"error": True}


# aStarPath("Arad", "Bucharest", nodes, adj)
# print(isPathAvailable("Arad", "Bucharest", nodes, adj))

print(aStarPath("A", "D", nodes, adj))
# print(isPathAvailable("A", "D", nodes, adj))