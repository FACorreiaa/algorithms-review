# def palindromePartiotioningMinCuts(string):
#     palindromes = [[False for i in string] for j in string]
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             palindromes[i][j] = isPalindrome(string[i:j+1])
#     cuts = [float("inf") for i in string]
#     for i in range(len(string)):
#         if palindromes[0][i]:
#             cuts[i] = 0
#         else:
#             cuts[i] = cuts[i - 1] + 1
#             for j in range(1, i):
#                 if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
#                     cuts[i] = cuts[j - 1] + 1
#     return cuts[-1]


# def isPalindrome(string):
#     leftId = 0
#     rightId = len(string) - 1
#     while leftId < rightId:
#         if string[leftId] != string[rightId]:
#             return False
#         leftId += 1
#         rightId -= 1
#     return True

# v2
# O(n2) time | O(n2) space
def palindromePartiotioningMinCuts(string):
    palindromes = [[False for i in string] for j in string]
    for i in range(len(string)):
        palindromes[i][i] = True
    for length in range(2, len(string) + 1):
        for i in range(0, len(string) - length + 1):

            j = i + length - 1
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]
    cuts = [float("inf") for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
    return cuts[-1]
