# Time O(n) | Space O(1)
def kadaneAlgo(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
