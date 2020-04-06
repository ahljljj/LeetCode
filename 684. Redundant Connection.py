'''
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.

Accepted
80,209
Submissions
144,050

'''

'''
2020/04/04, union find

Runtime: 56 ms, faster than 67.91% of Python3 online submissions for Redundant Connection.
Memory Usage: 14.3 MB, less than 14.29% of Python3 online submissions for Redundant Connection.

'''


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for edge in edges:
            for v in edge:
                nodes.add(v)
        union_find = UnionFind(nodes)
        for edge in edges:
            if not union_find.union(edge[0], edge[1]):
                return edge


class UnionFind:
    def __init__(self, nodes):
        self.parents = {x: x for x in nodes}
        self.size = {x: 1 for x in nodes}

    def find(self, A):
        root = A
        while root != self.parents[root]:
            root = self.parents[root]
        while A != root:
            old_root = self.parents[A]
            self.parents[A] = root
            A = old_root
        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY: return False
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        return True
