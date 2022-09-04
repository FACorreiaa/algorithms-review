# O(nc) time | O(nc) space
def knapsackProblem(items, capacity):
    knacksackValues = [[0 for x in range(0, capacity + 1)]
                       for y in range(0, len(items) + 1)]

    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1]
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knacksackValues[i][c] = knacksackValues[i - 1][c]
            else:
                knacksackValues[i][c] = max(
                    knacksackValues[i - 1][c], knacksackValues[i-1][c - currentWeight] + currentValue)
    return [knacksackValues[-1][-1], getknapSackItems(knacksackValues, items)]


def getknapSackItems(knacksackValues, items):
    sequence = []
    i = len(knacksackValues) - 1
    c = len(knacksackValues[0]) - 1
    while i > 0:
        if knacksackValues[i][c] == knacksackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
