# 1602. Find Nearest Right Node in Binary Tree


# 2021/01/28
# Runtime: 336 ms, faster than 23.30% of Python3 online submissions for Find Nearest Right Node in Binary Tree.
# Memory Usage: 52.3 MB, less than 23.35% of Python3 online submissions for Find Nearest Right Node in Binary Tree.

# standard bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        q = collections.deque([root])
        find = False
        while q:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                if find: return front
                if front == u: find = True
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            if find: return
        return
