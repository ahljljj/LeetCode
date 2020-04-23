'''
1315. Sum of Nodes with Even-Valued Grandparent


Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.



Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
Accepted
19,461
Submissions
23,330

'''

# 2020/04/22, dfs, haven't fully understand my thought, but it passed all tests

'''
Runtime: 96 ms, faster than 94.23% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, False, False, False)
        return self.res

    def dfs(self, root, is_grandparent, is_parent, is_kid):
        if not root: return
        if is_kid:
            self.res += root.val
            is_kid = False
        is_grandparent = root.val % 2 == 0
        is_kid = is_parent
        is_parent = is_grandparent
        self.dfs(root.left, is_grandparent, is_parent, is_kid)
        self.dfs(root.right, is_grandparent, is_parent, is_kid)


