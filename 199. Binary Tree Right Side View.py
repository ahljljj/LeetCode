"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


"""


#dfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(res, root, 0)
        return res
    
    def helper(self, res, root, level):
        #edge/condition
        if not root:
            return
        #append/condition
        if level == len(res):
            res.append(root.val)
        self.helper(res, root.right, level + 1)
        self.helper(res, root.left, level + 1)

# 2020/04/22, standard BFS

'''
Runtime: 28 ms, faster than 84.13% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.
'''

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = collections.deque([root])
        res = []
        while q:
            size = len(q)
            res.append(q[-1].val)
            for _ in range(size):
                front = q.popleft()
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
        return res