"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.




"""

'''
time limit exceeded

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0
        
        step = 1
        queue = [beginWord]
        dcty = self.hashmap(beginWord, wordList)
        while len(queue) > 0:
            tmp = []
            step += 1
            for word in queue:
                if word in dcty: tmp.extend(dcty[word])
                if endWord in tmp: return step
            queue = tmp        
        return 0
        
        
    def diff(self, l1, l2):
        count = 0
        for i in range(len(l1)):
            if l1[i] != l2[i]: count += 1
            if count > 1: return False
        return True
    
    def hashmap(self, beginword, wordlist):
        dcty = {}
        if beginword not in wordlist: wordlist.append(beginword)
        for word in wordlist:
            for neighbor in wordlist:
                if neighbor != word and self.diff(neighbor, word):
                    if word in dcty:
                        dcty[word].append(neighbor)
                    else:
                        dcty[word] = [neighbor]
        return dcty
        

'''