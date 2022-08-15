# Average O(Log(n)) time | O(log(n)) space
# Worst case O(n) time and space
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float("inf"))


# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         closest

# Average O(Log(n)) time | O(1) space
# Worst case O(1) time and space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):

    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = tree.left
        elif target > currentNode.value:
            currentNode = tree.right
        else:
            break
    return closest
