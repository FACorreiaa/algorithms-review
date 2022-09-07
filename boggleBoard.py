
# O(nm * 8s) + ws time | O(ws + nm)
def boggleBoard(board, words):
    tree = Tree()
    for word in words:
        tree.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, tree.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, treeNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in treeNode:
        return
    visited[i][j] = True
    TreeNode = treeNode[letter]
    if "*" in TreeNode:
        finalWords[TreeNode["*"]] = True
    neighbors = getNeighbours(i, j, board)
    for neighbors in neighbors:
        explore(neighbors[0], neightbors[1], board,
                TreeNode, visited, finalWords)
    visited[i][j] = False
