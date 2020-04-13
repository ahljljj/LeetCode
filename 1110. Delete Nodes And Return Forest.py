'''
1110. Delete Nodes And Return Forest


Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
Accepted
43,017
Submissions
65,466

'''

'''
2020/04/13, dfs, too clever

Runtime: 72 ms, faster than 46.09% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Delete Nodes And Return Forest.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        target = set(to_delete)
        self.dfs(root, True, target, res)
        return res

    def dfs(self, root, is_root, target, res):
        if not root: return None
        root_deleted = (root.val in target)
        if is_root and not root_deleted: res.append(root)
        root.left = self.dfs(root.left, root_deleted, target, res)
        root.right = self.dfs(root.right, root_deleted, target, res)
        return None if root_deleted else root
