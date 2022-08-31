# O(n2) time | O(n2) space
# def sameBST(arrayOne, arrayTwo):
#     if len(arrayOne) != len(arrayTwo):
#         return False

#     if len(arrayOne) == 0 and len(arrayTwo) == 0:
#         return True

#     if arrayOne[0] != arrayTwo[0]:
#         return False

#     leftOne = getSmaller(arrayOne)
#     leftTwo = getSmaller(arrayTwo)
#     rightOne = getBiggerOrEqual(arrayOne)
#     rightTwo = getBiggerOrEqual(arrayTwo)

#     return sameBST(leftOne, leftTwo) and sameBST(rightOne, rightTwo)


# def getSmaller(array):
#     smaller = []
#     for i in range(1, len(array)):
#         if array[i] < array[0]:
#             smaller.append(array[i])
#     return smaller


# def getBiggerOrEqual(array):
#     biggerOrEqual = []
#     for i in range(1, len(array)):
#         if array[i] >= array[0]:
#             biggerOrEqual.append(array[i])
#     return biggerOrEqual

# O(n2) time | O(n) space
def sameBST(arrayOne, arrayTwo):
    return areSameBST(arrayOne, arrayTwo, 0, float("-inf"), float("inf"))


def areSameBST(arrayOne, arrayTwo, rootIdOne, rootIdTwo, minVal, maxVal):
    if rootIdOne == -1 or rootIdTwo == -1:
        return rootIdOne == rootIdTwo

    if arrayOne[rootIdOne] != arrayTwo[rootIdTwo]:
        return False

    leftRootIdOne = getIdOfFirstSmaller(arrayOne, rootIdOne,  minVal)
    leftRootIdTwo = getIdOfFirstSmaller(arrayTwo, rootIdTwo,  minVal)
    rightRootIdOne = getIdOfFirstBiggerOrEqual(arrayOne, rootIdOne,  maxVal)
    rightRootIdTwo = getIdOfFirstBiggerOrEqual(arrayTwo, rootIdTwo,  maxVal)

    currentValue = arrayOne[rootIdOne]
    leftAreSame = areSameBST(
        arrayOne, arrayTwo, leftRootIdOne, leftRootIdTwo, minVal, currentValue)
    rightAreSame = areSameBST(
        arrayOne, arrayTwo, rightRootIdOne, rightRootIdTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame


def getIdOfFirstSmaller(array, startingId, minVal):
    for i in range((startingId + 1), len(array)):
        if array[i] < array[startingId] and array[i] >= minVal:
            return i
    return -1


def getIdOfFirstBiggerOrEqual(array, startingId, maxVal):
    for i in range(startingId + 1, len(array)):
        if array[i] >= array[startingId] and array[i] < maxVal:
            return i
    return -1
