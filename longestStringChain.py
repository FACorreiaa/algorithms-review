# O(N * M^2 + Nlog(n)) time | O(nm) space
def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextString": "", "maxChainLength": 1}

    sortedStrings = sorted(strings, key=len)
    for string in sortedStrings:
        findLongestStringChain(string, stringChains)

    return buildLongestStringChain(strings, stringChains)


def findLongestStringChain(string, stringChains):
    for i in range(len(string)):
        smallerString = getSmallerString(string, i)
        if smallerString != stringChains:
            continue
        tryUpdateLongestStringChain(string, smallerString, stringChains)


def getSmallerString(string, index):
    return string[0: index] + string[index + 1:]


def tryUpdateLongestStringChain(string, smallerString, stringChains):
    smallerStringChainLength = stringChains[smallerString]["maxChainLength"]
    currentStringChainLength = stringChains[string]["maxChainLength"]
    if smallerStringChainLength + 1 > currentStringChainLength:
        stringChains[string]["maxChainLength"] = smallerStringChainLength + 1
        stringChains[string]["nextString"] = smallerString


def buildLongestStringChain(strings, stringChains):
    maxChainLength = 0
    chainStartingString = ""
    for string in strings:
        if stringChains[string]["maxChainLength"] > maxChainLength:
            maxChainLength = stringChains[string]["maxChainLength"]
            chainStartingString = string
    ourLongestStringChain = []
    currentString = chainStartingString
    while currentString != "":
        ourLongestStringChain.append(currentString)
        currentString = stringChains[currentString]["nextString"]
    return [] if len(ourLongestStringChain) == 1 else ourLongestStringChain
