'''
1339. Maximum Product of Splitted Binary Tree

Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:



Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:



Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1


Constraints:

Each tree has at most 50000 nodes and at least 2 nodes.
Each node's value is between [1, 10000].
Accepted
9,415
Submissions
26,430

'''

# 2020/04/16, divide and conquer

'''
Runtime: 472 ms, faster than 16.16% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
Memory Usage: 66 MB, less than 100.00% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.total_sum = 0
        self.total_sum, _ = self.dfs(root)
        _, res = self.dfs(root)
        return res % (10 ** 9 + 7)

    def dfs(self, root):
        if not root: return 0, 0
        left_sum, left_max = self.dfs(root.left)
        right_sum, right_max = self.dfs(root.right)
        curr_sum = left_sum + root.val + right_sum
        curr_max = max([left_max, right_max, curr_sum * (self.total_sum - curr_sum)])
        return curr_sum, curr_max
