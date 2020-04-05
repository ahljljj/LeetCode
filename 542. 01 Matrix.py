'''
542. 01 Matrix

Share
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.


'''

'''
2020/04/05, BFS

Runtime: 668 ms, faster than 76.58% of Python3 online submissions for 01 Matrix.
Memory Usage: 16.7 MB, less than 8.33% of Python3 online submissions for 01 Matrix.
'''



class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        start = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 0]
        q = collections.deque(start)
        d = 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * m for _ in range(n)]
        while q:
            size = len(q)
            for _ in range(size):
                (x, y) = q.popleft()
                for (deltaX, deltaY) in dirs:
                    nx, ny = x + deltaX, y + deltaY
                    if -1 < nx < n and -1 < ny < m \
                    and not visited[nx][ny] and matrix[nx][ny]:
                        matrix[nx][ny] = d
                        q.append((nx, ny))
                        visited[nx][ny] = True
            d += 1
        return matrix