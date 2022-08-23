# O(w.h) time | O(w.h space)
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    # stack
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeughbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeughbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeughbors = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeughbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeughbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeughbors.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeughbors.append([i, j + 1])
    return unvisitedNeughbors
