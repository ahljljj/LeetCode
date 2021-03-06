"""
331. Verify Preorder Serialization of a Binary Tree


One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false

"""

'''
intuition

This is very simple problem if you use stacks. The key here is, when you see two consecutive "#" characters on stack, pop both of them and replace the topmost element on the stack with "#". For example,

preorder = 1,2,3,#,#,#,#

Pass 1: stack = [1]

Pass 2: stack = [1,2]

Pass 3: stack = [1,2,3]

Pass 4: stack = [1,2,3,#]

Pass 5: stack = [1,2,3,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,2,#]

Pass 6: stack = [1,2,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,#]

Pass 7: stack = [1,#,#] -> two #s on top so pop them and replace top with #. -> stack = [#]

If there is only one # on stack at the end of the string then return True else return False.

'''


class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '#':
            return True
        preorder = preorder.split(",")
        stack = []
        for node in preorder:
            stack.append(node)
            while self.endwithtwohashes(stack):
                stack.pop()
                stack.pop()
                stack[-1] = "#"
        return stack == ["#"]

    def endwithtwohashes(self, stack):
        if len(stack) < 3:
            return False
        if stack[-1] == stack[-2] == "#" and stack[-3] != "#":
            return True

