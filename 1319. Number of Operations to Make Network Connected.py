'''
1319. Number of Operations to Make Network Connected

There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1.



Example 1:



Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:



Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0


Constraints:

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
There are no repeated connections.
No two computers are connected by more than one cable.
Accepted
11,113
Submissions
21,609

'''

# 2020/04/26, standard union find

'''
Runtime: 864 ms, faster than 18.91% of Python3 online submissions for Number of Operations to Make Network Connected.
Memory Usage: 34 MB, less than 100.00% of Python3 online submissions for Number of Operations to Make Network Connected.
'''


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        union_find = UnionFind(n)
        group = n
        for u, v in connections:
            if union_find.union_find(u, v):
                group -= 1
        return group - 1 if group > 1 else 0


class UnionFind:
    def __init__(self, n):
        self.parents = {x: x for x in range(n)}
        self.size = {x: 1 for x in range(n)}

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
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            self.parents[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parents[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

