"""
245. Shortest Word Distance III


Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.


"""

# brute force


class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hashmap = {}
        for i, word in enumerate(words):
            if word not in hashmap:
                hashmap[word] = [i]
            else:
                hashmap[word].append(i)
        if word1 != word2:
            l1, l2 = hashmap[word1], hashmap[word2]
            return min([abs(x - y) for x in l1 for y in l2])
        l = hashmap[word1]
        res = len(words)
        for i in range(len(l) - 1):
            res = min(res, l[i + 1] - l[i])
        return res

