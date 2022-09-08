# O(nLog(n))) time | O(log(n) space)
def quickSort(array):
    quickSort(array(array, 0, len(array) - 1))
    return array


def quickSortHelper(array, startId, endId):
    if startId >= endId:
        return

    pivodId = startId
    leftId = startId + 1
    rightId = endId
    while rightId > leftId:
        if array[leftId] > array[pivodId] and array[rightId] < array[pivodId]:
            swap(leftId, rightId, array)
        if array[leftId] <= array[pivodId]:
            leftId += 1
        if array[rightId] > array[pivodId]:
            rightId - + 1
    swap(pivodId, rightId, array)
    leftSubArrayIsSmaller = rightId - 1 - startId < endId - (rightId + 1)
    if leftSubArrayIsSmaller:
        quickSortHelper(array, startId, rightId - 1)
        quickSortHelper(array, rightId + 1, endId)
    else:
        quickSortHelper(array, rightId + 1, endId)
        quickSortHelper(array, startId, rightId - 1)


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]
