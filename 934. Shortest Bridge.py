'''
934. Shortest Bridge

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1


'''

'''
2019/11/23

Runtime: 520 ms, faster than 43.42% of Python3 online submissions for Shortest Bridge.
Memory Usage: 13.7 MB, less than 64.71% of Python3 online submissions for Shortest Bridge.

'''


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # print(self.get_components(A))
        source, target = self.get_components(A)
        # print(source, target)
        q = collections.deque(source)
        # print(q)
        d = 0
        visited = set(source)
        n, m = len(A), len(A[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            breadth = len(q)
            for i in range(breadth):
                r, c = q.popleft()
                # print(r, c, 'd =', d)
                if (r, c) in target: return d - 1
                for (x, y) in dirs:
                    nr, nc = r + x, c + y
                    if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
                        continue
                    if (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            d += 1

    def get_components(self, A):
        n, m = len(A), len(A[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        components = []
        visited = set()
        for i in range(n):
            for j in range(m):
                if A[i][j] and (i, j) not in visited:
                    stack = [(i, j)]
                    done = set([(i, j)])
                    while stack:
                        r, c = stack.pop()
                        for d in dirs:
                            nr, nc = r + d[0], c + d[1]
                            if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
                                continue
                            if A[nr][nc] and (nr, nc) not in done:
                                stack.append((nr, nc))
                                done.add((nr, nc))
                    visited |= done
                    components.append(done)
        return components

