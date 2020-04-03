"""
261. Graph Valid Tree


Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.


"""

# bfs

'''

My solution is based on a simple idea that from any vertices, use BFS to visit the graph, if encountered the vertice that just been visited, or when finished visiting, there are still nodes that has not been visited, then this graph is not a valid tree.
There are two things that we need to pay attention:

The input edges are meant for directed graph, so first we need to cover it to the input for undirected graph.
2.User python's default dictionary to record vertices that has been visited, its a pretty convenient data structure for this problem.
'''

class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = {i: set() for i in range(n)}
        # initialization
        for (x, y) in edges:
            graph[x].add(y)
            graph[y].add(x)
        queue = collections.deque([0])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
                graph[neighbor].remove(node)
        return len(visited) == n

# dfs, brilliant

class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False
        graph = {i: set() for i in range(n)}
        # initialization
        for (x, y) in edges:
            graph[x].add(y)
            graph[y].add(x)
        visited = set()
        self.dfs(0, visited, graph)
        return len(visited) == n

    def dfs(self, node, visited, graph):
        if node in visited: return
        visited.add(node)
        for curr in graph[node]: self.dfs(curr, visited, graph)

# union find

class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False
        self.parents = {}
        self.rank = {}
        for (x, y) in edges:
            if x not in self.parents:
                self.parents[x] = x
                self.rank[x] = 1
            if y not in self.parents:
                self.parents[y] = y
                self.rank[y] = 1
            if self.parents[x] == self.parents[y]:
                return False
            self.union(x, y)
        return True

    def find(self, node):
        if node != self.parents[node]:
            p = self.parents[node]
            self.parents[node] = self.find(p)
        return self.parents[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            px, py = py, px
        if px != py:
            self.parents[px] = py
            self.rank[py] += self.rank[px]


# 2020/04/03, topological sorting

#Runtime: 92 ms, faster than 85.49% of Python3 online submissions for Graph Valid Tree.
#Memory Usage: 15.1 MB, less than 22.22% of Python3 online submissions for Graph Valid Tree.

# not a good solution, don't know why it can pass

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        # edge case
        if n == 1 and not edges: return True
        if len(edges) != n - 1: return False
        graph = self.get_graph(n, edges)
        in_degree = self.get_inDegree(graph)
        # start from vertex with in degree = 0
        # since every edge count twice, if there is any
        # in degree zero vertex, this graph is not connected
        # except there is only one node in the graph
        start = [x for x in graph if in_degree[x] == 1]
        q = collections.deque(start)
        count = 0
        # topological sorting: detect cycle or single point
        while q:
            front = q.popleft()
            count += 1
            for v in graph[front]:
                in_degree[v] -= 1
                if in_degree[v] == 1: q.append(v)
        # if there is a cycle or single point
        # then the count cann't equal to n
        return count == n

    def get_graph(self, n, edges):
        # initialize vertices
        m = {x: set() for x in range(n)}
        # get all edges
        for (v1, v2) in edges:
            m[v1].add(v2)
            m[v2].add(v1)
        return m

    def get_inDegree(self, graph):
        res = [0] * len(graph)
        for v in graph:
            for nei in graph[v]:
                res[nei] += 1
        return res
