"""
429. N-ary Tree Level Order Traversal


Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:







We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


"""

# bfs

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tmp = []
            tmpval = []
            for node in queue:
                tmpval.append(node.val)
                tmp.extend(node.children)
            res.append(tmpval)
            queue = tmp
        return res