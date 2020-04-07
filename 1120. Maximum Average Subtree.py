'''
1120. Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)



Example 1:



Input: [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.


Note:

The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
Accepted
9,234
Submissions
14,902

'''

'''
2020/04/07, divide and conquer

Runtime: 36 ms, faster than 99.45% of Python3 online submissions for Maximum Average Subtree.
Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Maximum Average Subtree.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        count, avg_sum, max_sum = self.helper(root)
        return max_sum

    def helper(self, root):
        if not root: return (0, 0, 0)
        left_size, left_sum, max_left = self.helper(root.left)
        right_size, right_sum, max_right = self.helper(root.right)

        curr_sum = left_sum * left_size + right_sum * right_size + root.val
        curr_size = 1 + left_size + right_size
        curr_avg = curr_sum / curr_size

        max_sum = max(max_left, max_right, curr_avg)

        return (curr_size, curr_avg, max_sum)
