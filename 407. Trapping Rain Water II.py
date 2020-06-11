'''
407. Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.





After the rain, water is trapped between the blocks. The total volume of water trapped is 4.



Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
Accepted
39,368
Submissions
94,755


'''


# 2020/06/11, heap + bfs

'''
Runtime: 208 ms, faster than 35.96% of Python3 online submissions for Trapping Rain Water II.
Memory Usage: 15.3 MB, less than 49.45% of Python3 online submissions for Trapping Rain Water II.
'''


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])
        q = []
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    q.append((heightMap[i][j], i, j))
                    visited[i][j] = True
        heapq.heapify(q)
        sea_level = -float("inf")
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        ans = 0
        while q:
            h, x, y = heapq.heappop(q)
            sea_level = max(sea_level, h)
            for delta_x, delta_y in dirs:
                nx = x + delta_x
                ny = y + delta_y
                if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                    continue
                ans += max(0, sea_level - heightMap[nx][ny])
                visited[nx][ny] = True
                heapq.heappush(q, (heightMap[nx][ny], nx, ny))
        return ans