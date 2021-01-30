# 1740. Find Distance in a Binary Tree

# 2021/01/28
# Runtime: 120 ms, faster than 100.00% of Python3 online submissions for Find Distance in a Binary Tree.
# # # Memory Usage: 22.9 MB, less than 100.00% of Python3 online submissions for Find Distance in a Binary Tree.

# 先用分治法找到最近祖先
# 再用层序遍历从这个最近祖先开始，分别求得到这两个结点的最短距离。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        lca = self.lowest_common_ancestor(root, p, q)
        queue = collections.deque([lca])
        # print(lca.val)
        level, count = 0, 2
        ans = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                front = queue.popleft()
                if front.val == p or front.val == q:
                    ans += level
                    count -= 1
                    if count == 0: return ans
                if front.left: queue.append(front.left)
                if front.right: queue.append(front.right)
            level += 1
        return ans

    def lowest_common_ancestor(self, root, p, q):
        if not root or root.val == q or root.val == p: return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left and right: return root
        if left: return left
        if right: return right
