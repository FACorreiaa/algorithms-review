# O(n^2) time | O(n) space
# def numberBinaryTopologies(n, cache={0: 1}):
#     if n is cache:
#         return cache[n]
#     numberOfTrees = 0
#     for leftTreeSize in range(n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfLeftTrees = numberBinaryTopologies(leftTreeSize, cache)
#         numberOfRightTrees = numberBinaryTopologies(rightTreeSize, cache)
#         numberOfTrees += numberOfRightTrees * numberOfLeftTrees
#     cache[n] = numberOfTrees
#     return numberOfTrees

# O(n ^ 2) time | O(n)
def numberBinaryTopologies(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = n - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]
