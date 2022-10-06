# O(n + m) time | O(m) space
def knuthMorrisPratt(string, substring):
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)


def buildPattern(substring):
    pattern = [-1 for i in substring]
    j = 0
    i = 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


def doesMatch(string, subString, pattern):
    i = 0
    j = 0
    while i + len(subString) - j <= len(string):
        if string[i] == subString[j]:
            if j == len(subString) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False
