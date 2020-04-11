"""
337. House Robber III


The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.



"""

'''

#dfs TLE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.map = {}
        self.helper(root, False)
        return self.res
    
    def helper(self, root, rob):
        if not root:
            return 0
        if not rob :
            self.res = max(self.helper(root.left, False) + self.helper(root.right,  False),
                       root.val + self.helper(root.left, True) + self.helper(root.right, True))
        else:
            self.res = self.helper(root.left, False) + self.helper(root.right, False)
        return self.res
            
            
            
'''


#leetcode solution(optimize)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.map = {}

        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0
        if root in self.map:
            return self.map[root]
        val = 0
        if root.left:
            val += self.helper(root.left.left) + self.helper(root.left.right)
        if root.right:
            val += self.helper(root.right.left) + self.helper(root.right.right)
        val = max(val + root.val, self.helper(root.left) + self.helper(root.right))
        if root not in self.map:
            self.map[root] = val
        return val




'''
Think one step further

In step I, we only considered the aspect of "optimal substructure", but think little about the possibilities of overlapping of the subproblems. For example, to obtain rob(root), we need rob(root.left), rob(root.right), rob(root.left.left), rob(root.left.right), rob(root.right.left), rob(root.right.right); but to get rob(root.left), we also need rob(root.left.left), rob(root.left.right), similarly for rob(root.right). The naive solution above computed these subproblems repeatedly, which resulted in bad time performance. Now if you recall the two conditions for dynamic programming: "optimal substructure" + "overlapping of subproblems", we actually have a DP problem. A naive way to implement DP here is to use a hash map to record the results for visited subtrees.

'''

#my solution: optimized by Leetcode's idea


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.map0 = {}
        self.map1 = {}
        #        self.helper(root, False)
        return self.helper(root, False)

    def helper(self, root, rob):
        if not root:
            return 0
        if rob == False and root in self.map0:
            return self.map0[root]
        elif rob == True and root in self.map1:
            return self.map1[root]
        if not rob:
            val = max(self.helper(root.left, False) + self.helper(root.right, False),
                      root.val + self.helper(root.left, True) + self.helper(root.right, True))
        else:
            val = self.helper(root.left, False) + self.helper(root.right, False)
        if rob == True:
            self.map1[root] = val
        else:
            self.map0[root] = val
        return val


# 2020/04/11, divide and conquer

'''
Runtime: 48 ms, faster than 69.18% of Python3 online submissions for House Robber III.
Memory Usage: 15.8 MB, less than 33.33% of Python3 online submissions for House Robber III.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        _, res = self.div_conq(root)
        return res

    def div_conq(self, root):
        if not root: return 0, 0
        prev_left, left = self.div_conq(root.left)
        prev_right, right = self.div_conq(root.right)
        curr_max = max(root.val + prev_left + prev_right, left + right)
        return left + right, curr_max