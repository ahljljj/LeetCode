"""
427. Construct Quad Tree


We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



It can be divided according to the definition above:





The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.



Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.

"""


# recursion


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        return self.dfs(grid)

    def dfs(self, grid):
        if not grid:
            return None

        n = len(grid)
        # topleft
        one, zero = False, False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    one = True
                else:
                    zero = True
        allone = True if (one and not zero) else False
        allzero = True if (zero and not one) else False
        if allone:
            return Node(True, True, None, None, None, None)
        if allzero:
            return Node(False, True, None, None, None, None)
        half = n // 2
        topleft = [[num for num in row[:half]] for row in grid[:half]]
        topright = [[num for num in row[half:]] for row in grid[:half]]
        botleft = [[num for num in row[:half]] for row in grid[half:]]
        botright = [[num for num in row[half:]] for row in grid[half:]]
        return Node(True, False, self.dfs(topleft), self.dfs(topright),
                    self.dfs(botleft), self.dfs(botright))
