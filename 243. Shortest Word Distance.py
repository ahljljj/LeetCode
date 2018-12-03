"""
243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


"""


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pair = set([word1, word2])
        dummy = set([word1, word2])
        res = len(words)
        for (i, word) in enumerate(words):
            if word in dummy:
                if len(pair) == 2:
                    start = i
                    pair.remove(word)
                else:
                    if word not in pair:
                        start = i
                    else:
                        res = min(res, i - start)
                        start = i
                        pair = set([word1, word2]) - pair
        return res


# simplify

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pair = set([word1, word2])
        dummy = set([word1, word2])
        res = len(words)
        for (i, word) in enumerate(words):
            if word in dummy:
                if len(pair) == 2:
                    pair.remove(word)
                elif word in pair:
                    res = min(res, i - start)
                    pair = set([word1, word2]) - pair
                start = i
        return res


