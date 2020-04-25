'''
737. Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].


Accepted
37,672
Submissions
83,302

'''


'''
2020/04/25, union find standard template

Runtime: 516 ms, faster than 46.29% of Python3 online submissions for Sentence Similarity II.
Memory Usage: 15.4 MB, less than 50.00% of Python3 online submissions for Sentence Similarity II.

'''


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        words = set()
        for x, y in zip(words1, words2):
            words.add(x)
            words.add(y)
        for x, y in pairs:
            words.add(x)
            words.add(y)
        union_find = UnionFind(words)
        for w1, w2 in pairs:
            union_find.union_find(w1, w2)
        for w1, w2 in zip(words1, words2):
            if union_find.find(w1) != union_find.find(w2):
                return False
        return True


class UnionFind:
    def __init__(self, words):
        self.parents = {word: word for word in words}
        self.size = {word: 1 for word in words}

    def find(self, x):
        root = x
        while root != self.parents[root]:
            root = self.parents[root]
        while root != x:
            old_root = self.parents[x]
            self.parents[x] = root
            x = old_root
        return root

    def union_find(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.size[root_x] < self.size[root_y]:
            self.parents[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parents[root_y] = root_x
            self.size[root_x] += self.size[root_y]















