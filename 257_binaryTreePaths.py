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