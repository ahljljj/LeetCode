'''
654. Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
Accepted
127,784
Submissions
161,103


'''

# 2020/06/17, dfs

'''
Runtime: 224 ms, faster than 58.67% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.2 MB, less than 41.97% of Python3 online submissions for Maximum Binary Tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return
        max_val = max(nums)
        i = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return root


# 2020/06/18, mono stack, too genius

'''
Runtime: 196 ms, faster than 90.95% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.5 MB, less than 5.04% of Python3 online submissions for Maximum Binary Tree.

思路：单调栈的代码总是很简洁，但是想法很精妙。一个结点node的父亲是左边第一个大于node的结点和右边第一个大于node的结点两个中较小的那个。

*每个值X的父亲一定是min{左边第一个比它大的值L，右边第一个比*
*它大的值R}*
*– ….., L, <X, …,<X, X, <X, …, <X, R,…*
*– 如果L<R，[L, R]里一定R先做根。然后[L, R)里L先做根，然后就是X*
*– 如果L>R， [L, R]里一定L先做根。然后(L, R]里R先做根，然后就是X*
'''

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nums.append(float("inf"))
        nodes = [TreeNode(num) for num in nums]
        stack = []
        for r in range(len(nums)):
            while stack and nums[stack[-1]] < nums[r]:
                top = stack.pop()
                l = stack[-1] if stack else len(nums)-1
                if nums[l] < nums[r]:
                    nodes[l].right = nodes[top]
                else:
                    nodes[r].left = nodes[top]
            stack.append(r)
        return nodes[-1].left