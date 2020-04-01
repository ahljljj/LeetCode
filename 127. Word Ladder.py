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
#time limit exceeded

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0

        step = 1
        queue = set([beginWord])
        dcty = self.hashmap(beginWord, wordList)
        while len(queue) > 0:
            tmp = set()
            step += 1
            for word in queue:
                if word in dcty:
                    for w in dcty[word]:
                        if w == endWord: return step
                        if w not in queue: tmp.add(w)
            queue = tmp
        return 0

    def diff(self, l1, l2):
        count = 0
        for i in range(len(l1)):
            if l1[i] != l2[i]: count += 1
        return count

    def hashmap(self, beginword, wordlist):
        dcty = {}
        if beginword not in wordlist: wordlist.append(beginword)
        for word in wordlist:
            for neighbor in wordlist:
                if self.diff(neighbor, word) == 1:
                    if word in dcty:
                        dcty[word].append(neighbor)
                    else:
                        dcty[word] = [neighbor]
                    if neighbor in dcty:
                        dcty[neighbor].append(word)
                    else:
                        dcty[neighbor] = [word]
        return dcty
'''

'''
# another TLE
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = set([beginWord])
        height = 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        newList = wordList[:]
        while queue:
            tmp = set()
            height += 1
            for cand in queue:
                if cand == endWord:
                    return height
                for word in wordList:
                    if word not in queue and self.diff(cand, word) == True:
                        newList.remove(word)
                        tmp.add(word)
            queue = tmp
            wordList= newList
        return 0
                
    
    
    def diff(self, word1, word2):
        count = 0
        for (w1, w2) in zip(word1, word2):
            if w1 != w2:
                count += 1
            if count > 1:
                return False
        return count == 1
'''


# TLE first, but change wordList to a set pass the test
'''
explanation

Performance note:

use set instead of list for dist
the order in if nw in dict and nw not in dist: is important. for long distance between start and end, dist can become huge while dict is of constant size.
Fun fact: when the size is small, list performs better.

In [125]: s = set()

In [126]: timeit s.add('1')
10000000 loops, best of 3: 89.1 ns per loop

In [127]: l = []

In [128]: timeit l.append('1')
10000000 loops, best of 3: 87.7 ns per loop

In [129]: timeit '1' in s
10000000 loops, best of 3: 44.9 ns per loop

In [130]: timeit '1' in l
10000000 loops, best of 3: 43.4 ns per loop

'''

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        xyz = "abcdefghijklmnopqrstuvwxyz"
        queue = set([beginWord])
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        height = 1
        while queue:
            height += 1
            tmp = set()
            for cand in queue:
                for i in range(len(cand)):
                    for c in xyz:
                        cand_copy = cand[:i] + c + cand[i + 1:]
                        if cand_copy in wordList:
                            if cand_copy == endWord:
                                return height
                            else:
                                tmp.add(cand_copy)
                                wordList.remove(cand_copy)
            queue = tmp
        return 0

#python, standard bfs

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        q = collections.deque([beginWord])
        cnt = 0
        d = 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)
        used = set()
        while q:
            length = len(q)
            cnt += 1
            for i in range(length):
                curr = q.popleft()
                used.add(curr)
                for i in range(len(curr)):
                    for ch in d:
                        new = curr[:i] + ch + curr[i + 1:]
                        if new not in wordList:
                            continue
                        if new == endWord:
                            return cnt + 1
                        if new not in used:
                            used.add(new)
                            q.append(new)
        return 0

# 2020/04/01, bfs, extreme slow

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        abc = "abcdefghijklmnopqrstuvwxyz"
        n = len(beginWord)
        q = collections.deque([beginWord])
        visited = set()
        res = 0
        while q:
            res += 1
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                visited.add(front)
                if front == endWord: return res
                for i in range(n):
                    for c in abc:
                        new_word = front[ : i] + c + front[i + 1: n]
                        if new_word not in wordList or new_word in visited: continue
                        q.append(new_word)
        return 0

#2020/04/01, remove word from wordlist can speed the running time

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        q = collections.deque([beginWord])
        res = 0
        while q:
            res += 1
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                if front == endWord: return res
                for new_word in self.get_next_word(front):
                    if new_word not in wordList: continue
                    wordList.remove(new_word)
                    q.append(new_word)
        return 0

    def get_next_word(self, word):
        res = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                res.append(word[:i] + c + word[i + 1:])
        return res


