'''
576. Out of Boundary Paths

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.



Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:



Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
Accepted
24,898
Submissions
72,927

'''


# 2020/04/15, memoization

'''
Runtime: 148 ms, faster than 71.56% of Python3 online submissions for Out of Boundary Paths.
Memory Usage: 16 MB, less than 33.33% of Python3 online submissions for Out of Boundary Paths.
'''

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0: return 0
        memo = {}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.dfs(m, n, dirs, N, i, j, memo)
        return memo[(i, j, N)]

    def dfs(self, m, n, dirs, move, i, j, memo):
        if (i, j, move) in memo: return memo[(i, j, move)] % (10 ** 9 + 7)
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        if move == 0:
            return 0
        curr = 0
        for deltaI, deltaJ in dirs:
            x, y = i + deltaI, j + deltaJ
            curr = (curr + self.dfs(m, n, dirs, move - 1, x, y, memo)) % (10 ** 9 + 7)
        memo[(i, j, move)] = curr
        return memo[(i, j, move)]