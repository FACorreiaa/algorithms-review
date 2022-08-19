# O(n^2) time | O(n) space
def getNthFib(n):
    if n == 2:
        return n
    elif n == 1:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n - 2)

# O(n) time | O(n) space


def getNthFibMemoized(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibMemoized(
            n-1, memoize) + getNthFibMemoized(n-2, memoize)
        return memoize[n]

# O(n) time | O(1) space


def interactiveNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
