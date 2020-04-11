'''
1214. Two Sum BSTs

Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.



Example 1:



Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9

'''

# 2020/04/10, inorder + binary search

'''
Runtime: 108 ms, faster than 38.65% of Python3 online submissions for Two Sum BSTs.
Memory Usage: 18.6 MB, less than 100.00% of Python3 online submissions for Two Sum BSTs.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        nums1, nums2 = [], []
        self.dfs(root1, nums1)
        self.dfs(root2, nums2)
        for num in nums1:
            if self.bin_search(nums2, target - num):
                return True
        return False

    def dfs(self, root, nums):
        if not root: return root
        self.dfs(root.left, nums)
        nums.append(root.val)
        self.dfs(root.right, nums)

    def bin_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m
            else:
                l = m
        if nums[l] == target or nums[r] == target:
            return True
        return False
