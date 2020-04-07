'''

257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''

#not my idea


class Solution:
    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if root != None:
            self.preOrder(root, "")
        return self.result

    def preOrder(self, root, path):
        if root.left == None and root.right == None:
            self.result.append(path + str(root.val))
        if root.left != None:
            self.preOrder(root.left, path + str(root.val) + "->")
        if root.right != None:
            self.preOrder(root.right, path + str(root.val) + "->")


'''
# 2020/04/07, divide and conquer
Runtime: 28 ms, faster than 82.85% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = self.div_conq(root)
        paths = []
        for p in res:
            paths.append('->'.join(map(str, p)))
        return paths

    def div_conq(self, root):
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        res = []
        left = self.div_conq(root.left)
        right = self.div_conq(root.right)
        for path in left:
            res.append([root.val] + path)
        for path in right:
            res.append([root.val] + path)
        return res

# slight modification

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        paths = []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        for path in left:
            paths.append(str(root.val) + '->' + path)
        for path in right:
            paths.append(str(root.val) + '->' + path)
        return paths


# traversal method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, res, [])
        return res

    def dfs(self, root, paths, path):
        if not root: return []
        path.append(str(root.val))
        if not root.left and not root.right:
            paths.append('->'.join(path))
        if root.left: self.dfs(root.left, paths, path)
        if root.right: self.dfs(root.right, paths, path)
        path.pop()