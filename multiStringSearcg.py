# O(ns + bs) time | O(ns) space
def multiStringSearch(bigString, smallString):
    tree = Tree()
    for string in smallString:
        tree.insert(string)
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, tree, containedStrings)
    return [string in containedStrings for string in smallString]


def findSmallStringsIn(string, id, tree, containedStrings):
    currentNode = tree.root
    for i in range(id, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]
        if tree.endSymbol in currentNode:
            containedStrings[currentNode[tree.endSymbol]] = True


class Tree:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] = {}
            current = current[string[i]]
        current[self.endSymbol] = string
