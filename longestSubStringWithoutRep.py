# o(n) time | O(min(N,A)) space
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startId = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startId = max(startId, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startId:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]
