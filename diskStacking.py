# O(n2) time | On) space
def diskStacking(disks):
    disks.sort = lambda disk: disk[2]
    heights = [disks[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightId = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if areValidDimentions(otherDisk, currentDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxHeightId]:
            maxHeightId = i
    return buildSequence(disks, sequences, maxHeightId)


def areValidDimentions(otherDisk, currentDisk):
    return otherDisk[0] < currentDisk[0] and otherDisk[1] < currentDisk[1] and otherDisk[2] < currentDisk[2]


def buildSequence(array, sequences, currentId):
    sequence = []
    while currentId is not None:
        sequence.append(array[currentId])
        currentId = sequences[currentId]
    return list(reversed(sequence))
