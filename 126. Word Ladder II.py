'''
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
Accepted
169,492
Submissions
806,075

'''


'''
2020/04/21, too hard

Runtime: 592 ms, faster than 36.04% of Python3 online submissions for Word Ladder II.
Memory Usage: 14.9 MB, less than 75.00% of Python3 online submissions for Word Ladder II.

'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        wordList.add(beginWord)
        if endWord not in wordList: return []
        d = {}
        self.bfs(wordList, endWord, d)
        res = []
        self.dfs(wordList, beginWord, endWord, res, [beginWord], d)
        return res

    def bfs(self, word_list, start, distance):
        q = collections.deque([start])
        visited = set([start])
        level = 0
        distance[start] = 0
        while q:
            size = len(q)
            level += 1
            for _ in range(size):
                front = q.popleft()
                distance[front] = level
                for word in self.get_next_word(front, word_list):
                    if word in distance: continue
                    q.append(word)
                    distance[word] = level
        return

    def get_next_word(self, word, word_dict):
        res = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for letter in letters:
                next_word = word[:i] + letter + word[i + 1:]
                if next_word != word and next_word in word_dict:
                    res.append(next_word)
        return res

    def dfs(self, word_list, start, end, res, path, distance):
        if start == end:
            res.append(path[:])
            return
        for next_word in self.get_next_word(start, word_list):
            if distance[next_word] != distance[start] - 1:
                continue
            path.append(next_word)
            self.dfs(word_list, next_word, end, res, path, distance)
            path.pop()
