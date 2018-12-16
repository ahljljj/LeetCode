'''
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

'''

# breadth first search

class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        nwse = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(rooms), len(rooms[0])
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        while queue:
            x, y = queue.popleft()
            for (i, j) in nwse:
                nx, ny = x + i, y + j
                if -1 < nx < n and -1 < ny < m and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append([nx, ny])
