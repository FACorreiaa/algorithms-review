# O(nLog(n)) time | O(n) space
def mergeSort(array):
    if len(array) <= 1:
        return array
    auxArray = array[:]
    mergeSortHelper(array, 0, len(array) - 1, auxArray)
    return array


def mergeSortHelper(mainArray, startId, endId, auxArray):
    if startId == endId:
        return
    middleId = (startId + endId) // 2
    mergeSortHelper(auxArray, startId, middleId, auxArray)
    mergeSortHelper(auxArray, middleId + 1, endId, auxArray)
    doMerge(mainArray, startId, middleId, endId, auxArray)


def doMerge(mainArray, startId, middleId, endId, auxArray):
    k = startId
    i = startId
    j = middleId + 1
    while i <= middleId and j <= endId:
        if auxArray[i] <= auxArray[j]:
            mainArray[k] = auxArray[i]
            i += 1
        else:
            mainArray[k] = auxArray[j]
            j += 1
        k += 1
    while i <= middleId:
        mainArray[k] = auxArray[i]
        i += 1
        k += 1
    while j <= endId:
        mainArray[k] = auxArray[j]
        j += 1
        k += 1
