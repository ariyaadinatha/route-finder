array = [["Bucharest", 44.457, 26.093],
         ["Arad", 46.181, 21.312],
         ["Zerind", 46.624, 21.518],
         ["Oradea", 47.089, 21.907],
         ["Sibiu", 45.794, 24.128],
         ["Fagaras", 45.842, 24.973],
         ["Timisoara", 45.756, 21.231],
         ["Lugoj", 45.691, 21.903],
         ["Mehadia", 44.904, 22.365],
         ["Drobeta", 44.639, 22.659],
         ["Cralova", 44.319, 23.794],
         ["Rimnicu Vilcea", 45.099, 24.369],
         ["Pitesti", 44.856, 24.869],
         ["Giurgiu", 43.905, 25.969],
         ["Urziceni", 44.718, 26.645],
         ["Neamt", 47.056, 26.506],
         ["Iasi", 47.158, 27.598],
         ["Vaslui", 46.641, 27.728],
         ["Hirsova", 44.690, 27.945],
         ["Eforie", 44.049, 28.653]]

# print("nodes: [")
# for i in array:
#     print("{")
#     print(f"\"longitude\": {i[1]},")
#     print(f"\"latitude\": {i[2]},")
#     print(f"\"name\": \"{i[0]}\"")
#     print("},")
# print("]")

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
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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


def getAdj(nodes, adj):
    size = len(nodes)
    index = 0
    for i in adj:
        indexAdj = 0
        print(f"\nkota : {nodes[index]['name']}")
        for j in i:
            # print(j)
            if (j == 1):
                print(f"tetangga : {nodes[indexAdj]['name']}")
            indexAdj += 1
        if (index != size-1):
            index += 1
        # print(size)
        # print(index)


getAdj(nodes, adj)
