'''
1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.



Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4



Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1


'''

'''
2019/11/23, python, bfs

Runtime: 736 ms, faster than 58.49% of Python3 online submissions for Shortest Path in Binary Matrix.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Shortest Path in Binary Matrix.


'''


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        n = len(grid)
        q = collections.deque([(0, 0)])
        visited = set([(0, 0)])
        d = 1
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while q:
            breadth = len(q)
            for i in range(breadth):
                r, c = q.popleft()
                if (r, c) == (n - 1, n - 1): return d
                for x, y in dirs:
                    nr, nc = r + x, c + y
                    if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
                        continue
                    if not grid[nr][nc] and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            d += 1
        return -1
