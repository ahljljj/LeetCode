"""
244. Shortest Word Distance II


Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


"""

# list compression, pre-processing


class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.map = {}
        for i, word in enumerate(words):
            if word not in self.map:
                self.map[word] = [i]
            else:
                self.map[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.map[word1]
        l2 = self.map[word2]
        return min([abs(x - y) for x in l1 for y in l2])

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)




# slight improvement O(n)
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.map = {}
        for i, word in enumerate(words):
            if word not in self.map:
                self.map[word] = [i]
            else:
                self.map[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.map[word1]
        l2 = self.map[word2]
        idx1, idx2 = 0, 0
        res = float('inf')
        while idx1 < len(l1) and idx2 < len(l2):
            res = min(res, abs(l2[idx2] - l1[idx1]))
            if l1[idx1] < l2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)