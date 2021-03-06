"""
117. Populating Next Right Pointers in Each Node II

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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL


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
        layer = [root]
        while len(layer) > 0:
            for i in range(len(layer)-1):
                layer[i].next = layer[i+1]
            layer[-1].next = None
            tmp = []
            for node in layer:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            layer = tmp

        return

# 2020/04/24, bfs, too simple but with extra space

'''
Runtime: 48 ms, faster than 73.12% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
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

# 2020/04/24, dfs

'''
Runtime: 56 ms, faster than 19.69% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root: return

        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.find_next(root)
        if root.right:
            root.right.next = self.find_next(root)

        self.dfs(root.right)
        self.dfs(root.left)

    def find_next(self, root):
        while root and root.next:
            root = root.next
            if root.left: return root.left
            if root.right: return root.right
        return None