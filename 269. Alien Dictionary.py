'''
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

'''

# 2020/04/03, topological sorting
#Runtime: 28 ms, faster than 88.75% of Python3 online submissions for Alien Dictionary.
#Memory Usage: 14 MB, less than 12.50% of Python3 online submissions for Alien Dictionary.

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.get_graph(words)
        in_degree = self.get_in_degree(graph)
        res = ""
        start = [s for s in graph if in_degree[s] == 0]
        q = collections.deque(start)
        while q:
            front = q.popleft()
            res += front
            for nei in graph[front]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0: q.append(nei)
        # if len(res) != len(graph), they might exist a cycle
        # which means the graph is invalid
        return res if len(res) == len(graph) else ""

    def get_order(self, word1, word2):
        # given two words: word1 and word2
        # detecting the corresponding order in character level
        i1, i2 = 0, 0
        while i1 < len(word1) and i2 < len(word2):
            if word1[i1] != word2[i2]: return (word1[i1], word2[i2])
            i1 += 1;
            i2 += 1
        return

    def get_graph(self, words):
        graph = {}
        # get all vertices
        for word in words:
            for c in word:
                if c not in graph: graph[c] = set()
        # get all edges, with key as starting vertex, and value as a set of vetex
        # representing the endpoint of the edge
        for i in range(len(words) - 1):
            order = self.get_order(words[i], words[i + 1])
            if order:
                graph[order[0]].add(order[1])
            # the graph is invalid, for example,"abc" < "ab"
            # which is impossible
            elif len(words[i]) > len(words[i + 1]):
                return {}
        return graph

    def get_in_degree(self, graph):
        m = {x: 0 for x in graph}
        for word in graph:
            for nei in graph[word]:
                m[nei] += 1
        return m