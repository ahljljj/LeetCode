'''
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)



Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
Accepted
24,626
Submissions
38,704

'''




'''
2020/04/13, divide and conquer
Runtime: 48 ms, faster than 20.26% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
Memory Usage: 18.7 MB, less than 88.89% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        _, _, res = self.div_conq(root)
        return res

    def div_conq(self, root):
        if not root: return float("inf"), -float("inf"), 0
        left_min, left_max, left_diff = self.div_conq(root.left)
        right_min, right_max, right_diff = self.div_conq(root.right)
        curr_min = min([left_min, right_min, root.val])
        curr_max = max([left_max, right_max, root.val])
        curr_diff = max([abs(root.val - left_min) if left_min != float("inf") else -float("inf"), \
                         abs(root.val - left_max) if left_max != -float("inf") else -float("inf"), \
                         abs(root.val - right_min) if right_min != float("inf") else -float("inf"), \
                         abs(root.val - right_max) if right_max != -float("inf") else - float("inf")])
        return curr_min, curr_max, max([left_diff, right_diff, curr_diff])
