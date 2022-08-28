class SuffixTree:
  def __init__(self, string):
    self.root = {}
    self.endSymbol = "*"
    self.populateSuffixTreeFrom(string)
  
  #O(n^2) time | O(n^2) space
  def populateSuffixTrieFrom(self, string):
    for i in range(len(string)):
      self.insertSubStringAt(i, string)

  def insertSubStringAt(self, i, string):
    node = self.root
    for j in range(i, len(string)):
      letter = string[j]
      if letter not in node:
        node[letter] = {}
      node = node[letter]
    node[self.endSymbol] = True

  #O(m) time where m is the input string | O(1) space
  def contains(self, string):
    node = self.root
    for letter in string:
      if letter not in node:
        return False
      node = node[letter]
    return seld.endSymbol in node
