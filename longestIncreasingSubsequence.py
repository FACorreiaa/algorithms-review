# O(nLogn) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    indices = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        newLength = binarySearchHelper(1, length, indices, array, num)
        sequences[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)
    return buildSequence(array, sequences, indices[length])


def binarySearchHelper(startId, endId, indices, array, num):
    if startId > endId:
        return startId
    middleId = (startId + endId) // 2
    if array[indices[middleId]] < num:
        startId = middleId + 1
    else:
        endId = middleId - 1
    return binarySearchHelper(startId, endId, indices, array, num)


def buildSequence(array, sequences, currentId):
    sequence = []
    while currentId is not None:
        sequences.append(array[currentId])
        currentId = sequences[currentId]
    return list(reversed(sequence))
