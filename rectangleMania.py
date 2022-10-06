# O(n2) time | O(n) space
def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)


def getCoordsTable(coords):
    coordsTable = {}
    for coord in coords:
        coordString = coordToString(coord)
        coordsTable[coordString] = True
    return coordsTable


def getRectangleCount(coords, coordsTable):
    rectangleCount = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not isInUpperRight():
                continue
            upperCoordString = coordToString([x1, y2])
            rightUpperString = coordToString([x2, y2])
            if upperCoordString in coordsTable and rightUpperString in coordsTable:
                rectangleCount += 1
    return rectangleCount


def isInUpperRight(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return x2 > x1 and y2 > y1


def coordToString(coord):
    x, y = coord
    return str(x) + '-' + str(y)
