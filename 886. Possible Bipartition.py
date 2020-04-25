'''
886. Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
Accepted
21,053
Submissions
49,135

'''


# 2020/04/25, graph based dfs, too hard

'''
Runtime: 776 ms, faster than 51.90% of Python3 online submissions for Possible Bipartition.
Memory Usage: 19.3 MB, less than 100.00% of Python3 online submissions for Possible Bipartition.
'''

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = self.make_graph(dislikes)
        colors = {}
        return all([self.dfs(graph, colors, i, 0) for i in range(1, N + 1) \
                    if i not in colors])

    def dfs(self, graph, colors, plp, color):
        if plp in colors:
            return colors[plp] == color
        colors[plp] = color
        for neighbor in graph[plp]:
            if not self.dfs(graph, colors, neighbor, color ^ 1):
                return False
        return True

    def make_graph(self, dislikes):
        m = collections.defaultdict(list)
        for (x, y) in dislikes:
            m[x].append(y)
            m[y].append(x)
        return m
