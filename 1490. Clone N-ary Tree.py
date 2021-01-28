# 1490. Clone N-ary Tree

# 2021/01/28
# Runtime: 116 ms, faster than 9.41% of Python3 online submissions for Clone N-ary Tree.
# Memory Usage: 18.3 MB, less than 15.55% of Python3 online submissions for Clone N-ary Tree.

# n叉树上的克隆，类似于lc 1485
# 先clone结点，再clone 结点之间的关系

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return
        node_copy = self.get_copy(root)
        q = collections.deque([root])
        while q:
            front = q.popleft()
            for kid in front.children:
                node_copy[front].children.append(node_copy[kid])
                q.append(kid)
        return node_copy[root]

    def get_copy(self, root):
        m = {}
        q = collections.deque([root])
        while q:
            front = q.popleft()
            m[front] = Node(front.val)
            for kid in front.children:
                q.append(kid)
        return m