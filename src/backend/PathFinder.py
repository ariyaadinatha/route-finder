import math

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

def gn(nodeProcessAwal, kotaNext, nodes, adj):
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

    g = gn(nodeProcessAwal, kotaNext, nodes, adj)
    nodeProcessNext["gn"] = g
    f += g

    nodeProcessNext["fn"] = f


    return nodeProcessNext


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

        nodeProcessCurrent["path"] = [nodeIndex for nodeIndex in nodeProcessCurrent["visited"]]
        nodeProcessCurrent["path"].append(indexKotaCurrent)

        nodeProcessCurrent["error"] = False


        return nodeProcessCurrent
    else :
        return {"error": True}
