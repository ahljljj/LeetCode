"""
173. Binary Search Tree Iterator


Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


"""


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.root or self.stack:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        node = self.root
        self.root = self.root.right
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# 2020/04/08, jiuzhang template

'''
Runtime: 76 ms, faster than 73.89% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.7 MB, less than 7.69% of Python3 online submissions for Binary Search Tree Iterator.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        dummy = TreeNode(None)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        dummy = self.stack.pop()
        top = dummy
        if top.right:
            top = top.right
            while top:
                self.stack.append(top)
                top = top.left
        return dummy.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack: return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()