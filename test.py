import os


# format coor (lon,lat)
# Menggunakan formula haversine

testMatix = []

# f(n) =  g(n) + h(n)
# g(n) = jarak dari posisiAwal ke n
# h(n) = jarak garis lurus ke posisiTujuan


def aStar(posisiAwal, posisiTujuan):
    print("a")


def readFile(namafile):
    uploadDir = (str(os.getcwd())+"/upload/")
    fileLoc = (uploadDir+namafile)
    with open(fileLoc) as fp:
        line = fp.readline()
        for i in line:
            print(i)
        # print(line)


def fileToGraph(namaFile):
    filepath = (str(os.getcwd())+"/upload/"+namaFile)
    # row = getRow(namaFile)
    # arraydaGra = [[] for i in range(row)]
    with open(filepath) as fp:
        line = fp.readline()
        # countIndex = 0
        index = 0
        while line:
            striped = (line.rstrip(".\n").split(", "))
            # arrayEdges = []
            for content in striped:
                #  print(content)
                if (index == 0):
                    n = content
                    index += 1
                    print(n)
                elif ((index == n)):
                    print(f"ini line ke {content}")
                # print(index)
                index += 1
                #     arrayEdges.append(content)
            # arraydaGra[countIndex] += [[vertices], arrayEdges]
            # countIndex += 1
            line = fp.readline()
    # return (arraydaGra)


fileToGraph("test2.txt")
