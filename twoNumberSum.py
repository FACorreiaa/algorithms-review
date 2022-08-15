# O(n2) time | O(1) space
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum
#             return [firstNum, secondNum]
#     return []

# O(n) time | O(n) space
# def twoNumberSum(array, targetSum)
#    nums = {}
#    for num in array
#       potentialNatch = targetSum - num
#       if potentialNatch in nums:
#           return [potentialNatch, num]
#       else:
#           nums[num] = True
#    return []

# O(nlogn) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


twoNumberSum([10, 2, 3, 45, 6, 1, 2, 3, 4, 5, 6, 1, 3, 4, 5, 5, 6, 7], 8)
