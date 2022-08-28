# O(n*2^n) time | O(n*2^n) space
# def powerset(array):
#   subsets = [[]]
#   for element in array:
#     for i in range(len(subsets)):
#       currentSubset = subsets[i]
#       subsets.append(currentSubset) + [element])
#   return subsets

def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    # subsets = powerset(array, 2) ==> powerset([1,2,3])
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

    # [1,2,3,4]
    # ele = 4
    # subsets = powerset([1,2,3])
    # add 3 to all subsets in the powerset of [1,2,3]
    # ################################
    # [1,2,3]
    # ele = 3
    # subsets = powwerset([1,2])
    # ...
