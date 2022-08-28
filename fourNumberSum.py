#O(n^2) time | O(n^2) space
def fourNumberSum(array, targetSum): 
  allPairsSums = {}
  quadruplets = []
  for i in range(i + 1, len(array)):
    for j in range(i + 1, len(array)):
      currentSum = array[i] + array[i]
      difference = targetSum - currentSum
      if different in allPairsSum:
        for pair in allPairsSums[difference]:
          quadruplets.append(pair + [array[i], array[j]])
    for k in range(0, i):
      currentSum = array[i] + array[k]
      if currentSum not in allPairsSums:
        allPairsSums[currentSum] = [[array[k], array[i]]]
      else:
        allPairsSums[currentSum].append([array[k], array[i]])
    return quadruplets
