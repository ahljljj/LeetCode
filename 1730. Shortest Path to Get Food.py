# 1730. Shortest Path to Get Food

# 2021/01/28

# Runtime: 476 ms, faster than 97.12% of Python3 online submissions for Shortest Path to Get Food.
# # Memory Usage: 15.3 MB, less than 87.24% of Python3 online submissions for Shortest Path to Get Food.

# 棋盘上的bfs
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        start = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '*']
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque(start)
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in dirs:
                    x, y = i + di, j + dj
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 'X':
                        continue
                    if grid[x][y] == '#': return level + 1
                    q.append((x, y))
                    grid[x][y] = 'X'
            level += 1
        return -1
