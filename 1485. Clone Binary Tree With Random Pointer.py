# 1485. Clone Binary Tree With Random Pointer

# 2021/01/28
# Runtime: 252 ms, faster than 37.84% of Python3 online submissions for Clone Binary Tree With Random Pointer.
# Memory Usage: 19.2 MB, less than 63.06% of Python3 online submissions for Clone Binary Tree With Random Pointer.

# 标准 bfs， 与之前图上的clone一样
# 先把每个node clone 出来
# 再把node - node 之间的关系clone出来
# 注意有环的存在，用visited避免遇到重复的结点

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root: return
        node_copy = self.get_copy(root)
        q = collections.deque([root])
        visited = set()
        while q:
            front = q.popleft()
            if front in visited: continue
            visited.add(front)
            if front.left:
                q.append(front.left)
                node_copy[front].left = node_copy[front.left]
            if front.right:
                q.append(front.right)
                node_copy[front].right = node_copy[front.right]
            if front.random:
                node_copy[front].random = node_copy[front.random]
                q.append(front.random)
        return node_copy[root]

    def get_copy(self, root):
        m = {}
        q = collections.deque([root])
        while q:
            front = q.popleft()
            if front not in m:
                m[front] = NodeCopy(front.val)
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
                if front.random: q.append(front.random)
        return m
