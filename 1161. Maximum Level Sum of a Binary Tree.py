# 1161. Maximum Level Sum of a Binary Tree

# 2021/01/27
#
# Runtime: 284 ms, faster than 86.89% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 18.5 MB, less than 59.52% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
#
#标准bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = collections.deque([root])
        level = 1
        max_sum = -float("inf")
        min_level = None
        while q:
            size = len(q)
            curr_sum = 0
            for _ in range(size):
                front = q.popleft()
                curr_sum += front.val
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                min_level = level
            level += 1
        return min_level
