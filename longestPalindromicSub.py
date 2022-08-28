#Time O(n^2) | Space O(n)
def longestPalindromicSubstring(string):
  currentLongest = [0,1]
  for i in range(1, len(string)):
      odd = getLongestPalFrom(string, i-1, i+1)
      even = getLongestPalFrom(string, i-1, i)
      longest = max(odd, even, key = lambda x: x[1] - x[0])
      currentLogest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalFrom(string, leftId, rightId):
    while leftId >= 0 and rightId < len(string):
        if string[leftId] != string[rightId]
         break
        leftId -= 1
        rightId += 1
    return [leftId + 1, rightId]

