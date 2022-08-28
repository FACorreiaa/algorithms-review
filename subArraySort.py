#O(n) time | O(1) space
def subArraySort(array):
  minOutOfOrder = float("inf")
  maxOutOfOrder = float("-inf")
  for i in range(len(array)):
    num = array[i]
    if isOutOfOrder(i, num, array):
      minOutOfOrder = min(minOutOfOrder, num)
      maxOutOfOrder = max(maxOutOfOrder, num)
  if minOutOfOrder == float("inf")
    return [-1, -1]
  subArrayLeftId = 0
  while minOutOfOrder >= array[subarrayLeftIdx]:
    subarrayLeftIdx += 1
  subarrayRightIdx = len(array) - 1
  while maxOutofOrder <= array[subarrayRightIdx]:
    subarrayRightIdx -= 1
  return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
  if i == 0:
    return num > array[i + 1]
  if i == len(array) - 1:
    return num < array[i - 1]
  return num > array[i + 1] or num < array[i - 1]
