"""
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



"""

'''
intution: bfs on graph


For a tree we can do some thing similar. We start from every end, by end we mean vertex of degree 1 (aka leaves). We let the pointers move the same speed. When two pointers meet, we keep only one of them, until the last two pointers meet or one step away we then find the roots.

It is easy to see that the last two pointers are from the two ends of the longest path in the graph.

The actual implementation is similar to the BFS topological sort. Remove the leaves, update the degrees of inner vertexes. Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left. What's left is our answer!

The time complexity and space complexity are both O(n).


'''




class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        neighbors = [[] for _ in range(n)]
        # contruct the neighbors from the graph
        for (i, j) in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)
        # find all leaves
        leaves = [i for i in range(len(neighbors)) if len(neighbors[i]) == 1]
        # there are at most two roots
        while n > 2:
            tmp = []
            n -= len(leaves)
            for i in leaves:
                j = neighbors[i].pop()
                neighbors[j].remove(i)
                if len(neighbors[j]) == 1:
                    tmp.append(j)
            leaves = tmp
        return leaves

# 2021/01/25, bfs + graph

# 这题很难，暴力可以做但是超时了
# 需要转化成拓扑排序，这点很难想到。
# 需要发现 middle point of the tree。怎么发现middle？从叶子出发，一层层的往里推进

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        neighbors = self.get_neighbors(n, edges)
        degrees = self.get_degree(n, edges)
        start = [node for node in range(n) if degrees[node] == 1]
        q = collections.deque(start)
        remaing_nodes = n
        while remaing_nodes > 2:
            size = len(q)
            remaing_nodes -= size
            for _ in range(size):
                front = q.popleft()
                for nei in neighbors[front]:
                    degrees[nei] -= 1
                    if degrees[nei] == 1:
                        q.append(nei)
        return list(q)

    def get_neighbors(self, n, edges):
        m = {i: [] for i in range(n)}
        for x, y in edges:
            m[x].append(y)
            m[y].append(x)
        return m

    def get_degree(self, n, edges):
        m = {i: 0 for i in range(n)}
        for x, y in edges:
            m[x] += 1
            m[y] += 1
        return m