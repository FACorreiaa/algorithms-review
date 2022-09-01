# O(n2) time | O(n) space
def maxSumIncreasingSub(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumId = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sum[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumId]:
            maxSumId = i
    return [sums[maxSumId], buildSequence(array, sequences, maxSumId)]


def buildSequence(array, sequences, currentId):
    sequence = []
    while currentId is not None:
        sequence.append(array[currentId])
        currentId = sequences[currentId]
    return list(reversed(sequence))
