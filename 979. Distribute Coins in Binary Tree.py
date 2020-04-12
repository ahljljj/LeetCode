'''
979. Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4


Note:

1<= N <= 100
0 <= node.val <= N
Accepted
31,772
Submissions
46,658



'''

# 2020/04/12， dfs, tree, math

'''
Runtime: 36 ms, faster than 64.45% of Python3 online submissions for Distribute Coins in Binary Tree.
Memory Usage: 13.8 MB, less than 16.67% of Python3 online submissions for Distribute Coins in Binary Tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return 0
        # if not root.left and not root.right: return abs(root.val - 1), root.val - 1
        left_excess = self.dfs(root.left)
        right_excess = self.dfs(root.right)
        self.res += abs(left_excess) + abs(right_excess)
        curr_excess = left_excess + right_excess + root.val - 1
        return curr_excess