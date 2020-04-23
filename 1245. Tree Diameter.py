'''
1245. Tree Diameter

Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.



Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation:
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.

'''

'''
2020/04/23, bfs, too hard, like course schedule

Runtime: 188 ms, faster than 74.75% of Python3 online submissions for Tree Diameter.
Memory Usage: 18.9 MB, less than 100.00% of Python3 online submissions for Tree Diameter.
'''


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = self.get_graph(edges)
        degree = self.get_degree(graph)
        start = [x for x in graph if degree[x] == 1]
        q = collections.deque(start)
        depth, prev_size = -1, None
        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                front = q.popleft()
                for nei in graph[front]:
                    degree[nei] -= 1
                    if degree[nei] == 1: q.append(nei)
        return depth * 2 if size == 1 else depth * 2 + 1

    def get_graph(self, edges):
        m = {}
        for u, v in edges:
            if u not in m:
                m[u] = set([v])
            else:
                m[u].add(v)
            if v not in m:
                m[v] = set([u])
            else:
                m[v].add(u)
        return m

    def get_degree(self, graph):
        m = {x: 0 for x in graph}
        for x in graph:
            m[x] += len(graph[x])
        return m


