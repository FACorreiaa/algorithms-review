# O(b2R) Time | O(b) Space
def apartmentHunting(blocks, reqs):
    maxDistanceAtBlocks = [float("-inf") for block in blocks]

    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(
                        closestReqDistance, distanceBetween(i, j))
            maxDistanceAtBlocks[i] = max(
                maxDistanceAtBlocks[i], closestReqDistance)
    return getIndexAtMinValue(maxDistanceAtBlocks)


def getIndexAtMinValue(array):
    idAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idAtMinValue = i
    return idAtMinValue


def distanceBetween(a, b):
    return abs(a - b)
