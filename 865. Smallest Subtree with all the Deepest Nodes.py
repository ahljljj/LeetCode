# 865. Smallest Subtree with all the Deepest Nodes


# Runtime: 36 ms, faster than 63.14% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
# Memory Usage: 14.5 MB, less than 35.55% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.


# 2021/01/26， bfs + divide conque
# 利用bfs 找到叶子层最左边和最右边的叶子，这两个叶子的least common accestor 决定了所有叶子的 lca
# 利用分治法求两个结点的lca
# 分治函数的定义，返回的是 lca，如果左边没找到返回右边，反之，返回左边的值
# 如果两边都有返回值？这点比较费解。。其实也比较好理解，分治函数返回lca的前提是root是p和q 一个common ancesstor
# 如果不是的话就返回 p 或者 q, 表明p 或者 q 至少有一个有这个子树中。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                front = q.popleft()
                if i == 0: left_most = front
                if i == size - 1: right_most = front
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
        ans = self.div_conq(root, left_most, right_most)
        return ans

    def div_conq(self, root, p, q):
        if not root or root == p or root == q: return root
        left = self.div_conq(root.left, p, q)
        right = self.div_conq(root.right, p, q)
        if not left: return right
        if not right: return left
        return root