'''
988. Smallest String Starting From Leaf

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)



Example 1:



Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:



Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:



Input: [2,2,1,null,1,0,null,0]
Output: "abc"


Note:

The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
Accepted
21,458
Submissions
47,581

'''

# 2020/04/12, backtracking

'''
Runtime: 52 ms, faster than 32.61% of Python3 online submissions for Smallest String Starting From Leaf.
Memory Usage: 15.1 MB, less than 50.00% of Python3 online submissions for Smallest String Starting From Leaf.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = chr(ord('z') + 1)
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, chars):
        if not root:
            return
        chars.append(chr(ord('a') + root.val))
        if not root.left and not root.right:
            string = ''.join(chars[::-1])
            if string < self.ans:
                self.ans = string
        self.dfs(root.left, chars)
        self.dfs(root.right, chars)
        chars.pop()

