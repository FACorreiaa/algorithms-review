# O(nLog(n)) time | O(1) space
def heapSort(array):
    buildMaxHeap(array)
    for endId in reversed(range(1, len(array))):
        swap(0, endId, array)
        siftDown(0, endId - 1, array)
    return array


def buildMaxHeap(array):
    firstParentId = (len(array) - 1) // 2
    for currentId in reversed(range(firstParentId + 1)):
        siftDown(currentId, len(array) - 1, array)


def siftDown(currentIdx, endId, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endId:
        childTwoIdx = currentIdx * 2 + 2 if currentId * 2 + 2 <= endId else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idx = childTwoIdx
        else:
            idx = childOneIdx
        if heap[idx] > heap[currentIdx]:
            swap(currentId, idx, heap)
            currentId = idx
            childOneIdx = currentId * 2 + 1
        else:
            return


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]
