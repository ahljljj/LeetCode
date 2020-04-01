"""
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if not root: return res

        queue = [root]
        layer = 0

        while len(queue) > 0:
            layer += 1
            if layer % 2 == 1:
                res.append([node.val for node in queue])
            else:
                res.append([node.val for node in queue][::-1])
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
        return res


# 2020/03/31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])
        res = []
        l_to_r = True
        while q:
            size = len(q)
            if l_to_r:
                R = range(size)
            else:
                R = range(size - 1, -1, -1)
            l_to_r = not l_to_r
            level = [0] * size
            for i in R:
                front = q.popleft()
                level[i] = front.val
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            res.append(level)
        return res

#2020/03/31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])
        res = []
        l_to_r = True
        while q:
            size = len(q)
            level = collections.deque([])
            for _ in range(size):
                if l_to_r:
                    front = q.popleft()
                    level.append(front.val)
                    if front.left: q.append(front.left)
                    if front.right: q.append(front.right)
                else:
                    front = q.pop()
                    level.append(front.val)
                    if front.right: q.appendleft(front.right)
                    if front.left: q.appendleft(front.left)
            res.append(list(level))
            l_to_r = not l_to_r
        return res