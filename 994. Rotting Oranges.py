# 994. Rotting Oranges

# 2021/01/27， standard  bfs

# Runtime: 68 ms, faster than 16.93% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 14.3 MB, less than 69.36% of Python3 online submissions for Rotting Oranges.

# 经典棋盘上的bfs

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
        if not fresh: return 0
        start = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]
        q = collections.deque(start)
        t = -1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in dirs:
                    x, y = i + di, j + dj
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                        continue
                    q.append((x, y))
                    grid[x][y] = 2
            t += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return t


