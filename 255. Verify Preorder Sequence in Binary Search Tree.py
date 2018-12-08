"""
255. Verify Preorder Sequence in Binary Search Tree


Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree:

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?


"""


# py stack with extra space


class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = -float('inf')
        stack = []
        for node in preorder:
            if node < low:
                return False
            while stack and node > stack[-1]:
                low = stack.pop()
            stack.append(node)
        return True

