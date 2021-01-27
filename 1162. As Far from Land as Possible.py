# 1162. As Far from Land as Possible


# 2021/01/27
# Runtime: 540 ms, faster than 83.88% of Python3 online submissions for As Far from Land as Possible.
# Memory Usage: 15.2 MB, less than 50.31% of Python3 online submissions for As Far from Land as Possible.

# 反向思考的 bfs
# 从所有的land开始层序遍历，遇到水池就标记住。最后无法继续的时候的层数就是某个水池离land最近的距离，也就是最终答案。

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        start = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
        if len(start) == n * m: return -1
        q = collections.deque(start)
        level = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in dirs:
                    x, y = i + di, j + dj
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 0: continue
                    grid[x][y] = 1
                    q.append((x, y))
            level += 1
        return level

