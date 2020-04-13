'''
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.


Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
Accepted
26,411
Submissions
31,625


'''



'''
2020/04/12, BFS, although it is labeled as dfs, bfs is easier

Runtime: 92 ms, faster than 83.79% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Deepest Leaves Sum.



'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        q = collections.deque([root])
        while q:
            size = len(q)
            res = 0
            for _ in range(size):
                front = q.popleft()
                res += front.val
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
        return res