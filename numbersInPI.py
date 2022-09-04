# def numbersInPI(pi, numbers):
#     numbersTable = {number: True for number in numbers}
#     minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
#     return -1 if minSpaces == float("inf") else minSpaces


# def getMinSpaces(pi, numbersTable, cache, id):
#     if id == len(pi):
#         return 0
#     if id in cache:
#         return cache[id]
#     minSpaces = float("inf")
#     for i in range(id, len(pi)):
#         prefix = pi[id:i + 1]
#         if prefix in numbersTable:
#             minNumberSpacesInSuffix = getMinSpaces(
#                 pi, numbersTable, cache, i + 1)
#             minSpaces = min(minSpaces, minNumberSpacesInSuffix + 1)
#             # 31456
#     cache[id] = minSpaces
#     return cache[id]

# O(n3 + m) time | O(n + m) space
def numbersInPI(pi, numbers):
    numbersTable = {number: True for number in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]


def getMinSpaces(pi, numbersTable, cache, id):
    if id == len(pi):
        return 0
    if id in cache:
        return cache[id]
    minSpaces = float("inf")
    for i in range(id, len(pi)):
        prefix = pi[id:i + 1]
        if prefix in numbersTable:
            minNumberSpacesInSuffix = getMinSpaces(
                pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minNumberSpacesInSuffix + 1)
            # 31456
    cache[id] = minSpaces
    return cache[id]
