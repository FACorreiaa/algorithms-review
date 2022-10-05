# O(b2R) Time | O(b) Space
# def apartmentHunting(blocks, reqs):
#     maxDistanceAtBlocks = [float("-inf") for block in blocks]

#     for i in range(len(blocks)):
#         for req in reqs:
#             closestReqDistance = float("inf")
#             for j in range(len(blocks)):
#                 if blocks[j][req]:
#                     closestReqDistance = min(
#                         closestReqDistance, distanceBetween(i, j))
#             maxDistanceAtBlocks[i] = max(
#                 maxDistanceAtBlocks[i], closestReqDistance)
#     return getIndexAtMinValue(maxDistanceAtBlocks)


# def getIndexAtMinValue(array):
#     idAtMinValue = 0
#     minValue = float("inf")
#     for i in range(len(array)):
#         currentValue = array[i]
#         if currentValue < minValue:
#             minValue = currentValue
#             idAtMinValue = i
#     return idAtMinValue


# def distanceBetween(a, b):
#     return abs(a - b)

# O(br) time | O(br) space
def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(
        map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(
        blocks, minDistancesFromBlocks)
    return getIndexAtMinValue(maxDistancesAtBlocks)


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(
            map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)


def getIndexAtMinValue(array):
    idAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idAtMinValue = i
    return idAtMinValue


def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqDistance = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqDistance = i
        minDistances[i] = distanceBetween(i, closestReqDistance)
    for i in reversed(range(blocks)):
        if blocks[i][req]:
            closestReqDistance = i
        minDistances[i] = min(
            minDistances[i], distanceBetween(i, closestReqDistance))
    return minDistances


def distanceBetween(a, b):
    return abs(a - b)
