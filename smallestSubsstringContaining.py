# O(b + s) time | O(b + s) space
def smallestSubstringContaining(bigString, smallString):
    targetCharCount = getCharCount(smallString)
    substringBounds = getSubstringBounds(bigString, targetCharCount)
    return getSubstringBounds(bigString, substringBounds)


def getCharCount(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts


def getSubstringBounds(string, targetCharCounts):
    substringBounds = [0, float("inf")]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    numUniqueCharsDone = 0
    leftId = 0
    rightId = 0
    while rightId < len(string):
        rightChar = string[rightId]
        if rightChar not in targetCharCounts:
            rightId += 1
            continue
        increaseCharCount(rightChar, substringCharCounts)
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1
        while numUniqueCharsDone == numUniqueChars and leftId <= rightId:
            substringBounds = getCloserBounds(
                leftId, rightId, substringBounds[0], substringBounds[1])
            leftChar = string[leftId]
            if leftChar not in targetCharCounts:
                leftId += 1
                continue
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            decreaseCharCount(leftChar, substringCharCounts)
            leftId += 1
    rightId += 1


def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[start: end + 1]


def getCloserBounds(id1, id2, id3, id4):
    return [id1, id2] if id2 - id1 < id4 - id3 else [id3, id4]


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1
