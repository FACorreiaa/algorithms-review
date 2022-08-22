# [7, 10, 12, 7, 9, 14]

# Solution = 7+12+14 = 33
# [7, 10, 19, 28, 33]
# maxSums[i] = maxSum[i-1] or maxSum[i-2] + array[i]

# O(n) time | O(n) Space
# def maxSubsetSumNoAdjacent(array):
#     if not len(array):
#         return
#     elif len(array) == 1:
#         return array[0]
#     maxSums = array[:]
#     maxSums[1] = max(array[0], array[1])
#     for i in range(2, len(array)):
#         maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
#     return maxSums[-1]

# O(n) time | O(1) Space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
