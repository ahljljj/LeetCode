"""
417. Pacific Atlantic Water Flow


Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).



"""

'''
wrong ans

class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        accessible = [[None]* m for _ in range(n)] 
        self.memo = {}

        for i in range(n):
            accessible[i][0] = 1
            accessible[i][m - 1] = 2
        for i in range(m):
            accessible[0][i] = 1
            accessible[n - 1][i] = 2
        accessible[0][m - 1] = accessible[n - 1][0] = 3
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if accessible[i][j] == None:
                    self.helper(matrix, accessible, i, j)

#        for i in range(n):
#            accessible[i][0] = self.helper2(matrix, accessible, i, 0)
#            accessible[i][m - 1] = self.helper2(matrix, accessible, i, m - 1)

#        for i in range(m):
#            accessible[0][i] = self.helper2(matrix, accessible, 0, i)
#            accessible[n - 1][i] = self.helper2(matrix, accessible, n - 1, i)

#        print(accessible)
        res = []
        for i in range(n):
            for j in range(m):
                if accessible[i][j] >= 3:
                    res.append([i, j])

        return res


    def helper(self, matrix, accessible, i, j):
#        print("i, j", i, j, accessible[i][j])
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if accessible[i][j] == 3:
            return 3
        n = len(matrix)
        m = len(matrix[0])
        curr =  0
        if i - 1 >= 0 and matrix[i][j] >= matrix[i - 1][j]:
#            print("1")
            tmp = self.helper(matrix, accessible, i - 1, j)
#            print(tmp)
            if tmp != None:
                if tmp == 3:
                    self.memo[(i - 1, j)] = 3
                    return 3
                elif tmp != curr:
                    curr += tmp

        if i + 1 < n and matrix[i][j] >= matrix[i + 1][j]:
            tmp = self.helper(matrix, accessible, i + 1, j)
            if tmp != None:
                if tmp == 3:
                    self.memo[(i + 1, j)] = 3
                    return 3
                elif tmp != curr:
                    curr += tmp  
        if j - 1 >= 0 and matrix[i][j] >= matrix[i][j - 1]:
            tmp = self.helper(matrix, accessible, i, j - 1)
            if tmp != None:
                if tmp == 3:
                    self.memo[(i, j - 1)] = 3
                    return 3
                elif tmp != curr:
                    curr += tmp  
        if j + 1 < m and matrix[i][j] >= matrix[i][j + 1]:
            tmp = self.helper(matrix, accessible, i, j + 1)
            if tmp != None:
                if tmp == 3:
                    self.memo[(i, j + 1)] = 3
                    return 3
                elif tmp != curr:
                    curr += tmp
#        print("curr", curr)
        self.memo[(i, j)] = curr
        return curr


'''


'''
intuition

The DFS solution is straightforward. Starting from each point, and dfs its neighbor if the neighbor is equal or less than itself. And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point or not. Finally go through all nodes again and see if it can be both reached by two oceans. The trick is if a node is already visited, no need to visited again. Otherwise it will reach the recursion limits.


'''

# dfs

class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # start from the four edge: (*, 0) (*, m - 1), (0, *), (n - 1, *)
        for i in range(n):
            self.dfs(matrix, m, n, pacific, i, 0)
            self.dfs(matrix, m, n, atlantic, i, m - 1)
        for i in range(m):
            self.dfs(matrix, m, n, pacific, 0, i)
            self.dfs(matrix, m, n, atlantic, n - 1, i)
        res = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, m, n, visited, i, j):
        visited[i][j] = True  # initialization
        for (x, y) in self.directions:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and matrix[ni][nj] >= matrix[i][j]:
                self.dfs(matrix, m, n, visited, ni, nj)


# standard bfs


class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # start from the four edge: (*, 0) (*, m - 1), (0, *), (n - 1, *)
        for i in range(m):
            queue = set([(0, i)])
            self.bfs(matrix, m, n, pacific, queue)
            queue = set([(n - 1, i)])
            self.bfs(matrix, m, n, atlantic, queue)

        for i in range(n):
            queue = set([(i, 0)])
            self.bfs(matrix, m, n, pacific, queue)
            queue = set([(i, m - 1)])
            self.bfs(matrix, m, n, atlantic, queue)

        res = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def bfs(self, matrix, m, n, visited, queue):
        while queue:
            tmp = set()
            for (i, j) in queue:
                visited[i][j] = True
                for (x, y) in self.directions:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and matrix[ni][nj] >= matrix[i][j]:
                        tmp.add((ni, nj))
            queue = tmp


# 2020/04/18, two bfs

'''
Runtime: 408 ms, faster than 20.92% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.1 MB, less than 10.00% of Python3 online submissions for Pacific Atlantic Water Flow.
'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        n, m = len(matrix), len(matrix[0])
        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]
        pac_start = [(i, j) for i in range(n) for j in range(m) if i == 0 or j == 0]
        pac_q = collections.deque(pac_start)
        self.bfs(matrix, n, m, pac_q, pacific)
        alt_start = [(i, j) for i in range(n) for j in range(m) if i == n - 1 or j == m - 1]
        alt_q = collections.deque(alt_start)
        self.bfs(matrix, n, m, alt_q, atlantic)
        res = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def bfs(self, matrix, n, m, q, visited):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for (i, j) in q:
            visited[i][j] = True
        while q:
            i, j = q.popleft()
            for deltaI, deltaJ in dirs:
                x, y = i + deltaI, j + deltaJ
                if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or matrix[x][y] < matrix[i][j]: continue
                q.append((x, y))
                visited[x][y] = True








