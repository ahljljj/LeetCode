'''
272. Closest Binary Search Tree Value II

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Accepted
52,428
Submissions
106,551

'''

# 2020/04/08, iterative of inorder transversal + two pointers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        i, nums = self.inorder(root, target)
        l, r = i, i + 1
        res = []
        for _ in range(k):
            if l < 0:
                res.append(nums[r])
                r += 1
                continue
            if r >= len(nums):
                res.append(nums[l])
                l -= 1
                continue
            if abs(nums[l] - target) < abs(nums[r] - target):
                res.append(nums[l])
                l -= 1
            else:
                res.append(nums[r])
                r += 1
        return res

    def inorder(self, root, target):
        dummy = TreeNode(None)
        dummy.right = root
        stack = [dummy]
        nums, i = [], 0
        pos, res = None, float("inf")
        while stack:
            top = stack.pop()
            if top.right:
                top = top.right
                while top:
                    stack.append(top)
                    top = top.left
            if stack:
                curr = stack[-1].val
                nums.append(curr)
                if abs(curr - target) < abs(res - target):
                    pos = i
                    res = curr
            i += 1
        return pos, nums






