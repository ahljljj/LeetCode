"""
426. Convert Binary Search Tree to Sorted Doubly Linked List


Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:





We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.





Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.


"""


# dfs, too hard

'''

step1: inorder tranversal by recursion to connect the original BST
step2: connect the head and tail to make it circular

Tips: Using dummy node to handle corner case
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        self.prev = dummy = Node(None, None, None)
        self.dfs(root)
        self.prev.right = dummy.right
        dummy.right.left = self.prev
        return dummy.right

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.dfs(root.right)

# divide and conquer

'''
Step 1: Divide:
We divide tree into three parts: left subtree, root node, right subtree.
Convert left subtree into a circular doubly linked list as well as the right subtree.
Be careful. You have to make the root node become a circular doubly linked list.

Step 2: Conquer:
Firstly, connect left circular doubly linked list with the root circular doubly linked list.
Secondly, connect them with the right circular doubly linked list. Here we go!

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        lHead = self.treeToDoublyList(root.left)
        rHead = self.treeToDoublyList(root.right)
        # make root to be a cycle
        root.left = root
        root.right = root
        return self.join(self.join(lHead, root), rHead)

    def join(self, n1, n2):  # n1, n2: head (node with smallest value) of the two cycles
        if not n1:
            return n2
        if not n2:
            return n1
        tail1 = n1.left
        tail2 = n2.left
        tail1.right = n2
        n2.left = tail1
        tail2.right = n1
        n1.left = tail2
        # return the head n1 (the node with the smallest value in the new cycle)
        return n1



