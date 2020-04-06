'''
1135. Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.



Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation:
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation:
There is no way to connect all cities even if all edges are used.


Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]
Accepted
10,724
Submissions
18,973


'''

'''
2020/04/06, union find, solved after checking the hint:
Sort the edges by their cost and use a union-find data structure.

Runtime: 1328 ms, faster than 11.72% of Python3 online submissions for Connecting Cities With Minimum Cost.
Memory Usage: 19.5 MB, less than 100.00% of Python3 online submissions for Connecting Cities With Minimum

'''


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        union_find = UnionFind(N)
        cost = 0
        group = N
        for conn in connections:
            if union_find.union(conn[0], conn[1]):
                group -= 1
                cost += conn[2]
                if group == 1: return cost
        return -1


class UnionFind:
    def __init__(self, n):
        self.parents = {x + 1: x + 1 for x in range(n)}
        self.size = {x + 1: 1 for x in range(n)}

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