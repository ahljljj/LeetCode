'''
959. Regions Cut By Slashes

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.



Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:



Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
Accepted
15,047
Submissions
23,045

'''

'''
2020/04/04, union find, very hard, see md

Runtime: 672 ms, faster than 10.20% of Python3 online submissions for Regions Cut By Slashes.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Regions Cut By Slashes.

'''


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        nodes = [(i, j, k) for i in range(n) for j in range(n) for k in range(4)]
        union_find = UnionFind(nodes)
        for i in range(n):
            for j in range(n):
                if i < n - 1: union_find.union((i, j, 0), (i + 1, j, 2))
                if j < n - 1: union_find.union((i, j, 1), (i, j + 1, 3))
                if grid[i][j] == "\\":
                    union_find.union((i, j, 1), (i, j, 2))
                    union_find.union((i, j, 3), (i, j, 0))
                elif grid[i][j] == "/":
                    union_find.union((i, j, 0), (i, j, 1))
                    union_find.union((i, j, 2), (i, j, 3))
                else:
                    union_find.union((i, j, 0), (i, j, 1))
                    union_find.union((i, j, 1), (i, j, 2))
                    union_find.union((i, j, 2), (i, j, 3))
        return sum(union_find.find(x) == x for x in nodes)


class UnionFind:
    def __init__(self, nodes):
        self.parents = {x: x for x in nodes}
        self.size = {x: 1 for x in nodes}

    def find(self, A):
        root = A
        while root != self.parents[root]:
            root = self.parents[root]
        while A != root:
            old_root = self.parents[A]
            self.parents[A] = root
            A = old_root
        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]
