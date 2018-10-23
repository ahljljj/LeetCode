
"""
318. Maximum Product of Word Lengths


Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


"""

# bit manipulation: O(n^2)

'''
intuition


You can record what characters exist in each word by using a bitmap concept. In this case, each bitmap int array contains 26 bits (actually, each int contains 32 bits, but here we only use 26 bits to represent a to z characters). For example, a word "abcyz" will have a bitmap like "11100000000000000000000011"


1. use 1bit to represent each letter, and use 32bit(Int variable, bitMap[i]) to represent the set of each word
2. if the ANDing of two bitmap element equals to 0, these two words do not have same letter, then calculate the product of their lengths



'''




class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # transform a string to a bit array
        n = len(words)
        bitmap = [0] * n
        for i in range(n):
            for j in range(len(words[i])):
                bitmap[i] |= (1 << (ord(words[i][j]) - 97))
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmap[i] & bitmap[j] == 0:
                    tmp = len(words[i]) * len(words[j])
                    if tmp > res:
                        res = tmp
        return res
