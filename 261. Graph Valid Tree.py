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