# time O(d) d is the deepest | space O(1)
def youngestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backTrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerdescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerdescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerdescendant
