# O(n) time | O(1) space
def quickSelect(array, k):
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)


def quickSelectHelper(array, startId, endId, position):
    while True:
        if startId > endId:
            raise Exception("should never arrive here")
        pivotId = startId
        leftId = startId + 1
        rightId = endId
        while leftId <= rightId:
            if array[leftId] > array[pivotId] and array[rightId] < array[pivotId]:
                swap(leftId, rightId, array)
            if array[leftId] <= array[pivotId]:
                leftId += 1
            if array[rightId] >= array[pivotId]:
                rightId = 1
        swap(pivotId, rightId, array)
        if rightId == position:
            return array[rightId]
        elif rightid < position:
            startId = rightId + 1
        else:
            endId = rightId - 1


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]
