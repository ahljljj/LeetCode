'''
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

Accepted
73,935
Submissions
183,741

'''

# 2020/06/03, union find

'''

Runtime: 660 ms, faster than 34.60% of Python3 online submissions for Number of Islands II.
Memory Usage: 20.1 MB, less than 25.00% of Python3 online submissions for Number of Islands II.
'''


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        union_find = UnionFind(m, n)
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = []
        for i, j in positions:
            if (i, j) in visited:
                res.append(union_find.group)
                continue
            union_find.group += 1
            for delta_i, delta_j in dirs:
                n_i, n_j = i + delta_i, j + delta_j
                if n_i < 0 or n_i >= m or n_j < 0 or n_j >= n or (n_i, n_j) not in visited:
                    continue
                union_find.union((i, j), (n_i, n_j))
            res.append(union_find.group)
            visited.add((i, j))
        return res


class UnionFind:
    def __init__(self, n, m):
        self.partents = {(i, j): (i, j) for i in range(n) for j in range(m)}
        self.size = {(i, j): 1 for i in range(n) for j in range(m)}
        self.group = 0

    def find(self, node):
        root = node
        while root != self.partents[root]:
            root = self.partents[root]
        while root != node:
            old_root = self.partents[node]
            self.partents[node] = root
            node = old_root
        return root

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.group -= 1
        if self.size[root_x] < self.size[root_y]:
            self.partents[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.partents[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

