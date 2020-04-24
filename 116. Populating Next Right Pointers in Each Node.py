"""
116. Populating Next Right Pointers in Each Node

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL


"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root: return
        root.next = None
        self.helper(root)

        return

    def helper(self, root):

        if root == None: return
        if root.left: root.left.next = root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.helper(root.left)
        self.helper(root.right)

# python, bfs

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        q = collections.deque([root])
        while q:
            breadth = len(q)
            for i in range(breadth - 1):
                curr = q.popleft()
                if q: curr.next = q[0]
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            curr = q.popleft()
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)

# 2020/04/23,  bfs, not constant space

'''
Runtime: 56 ms, faster than 96.11% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                front = q.popleft()
                if i < size - 1:
                    front.next = q[0]
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
        return root








