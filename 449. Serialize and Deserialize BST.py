"""
449. Serialize and Deserialize BST


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


"""

# dfs/ preorder

'''

Hi all, I think my solution is pretty straightforward and easy to understand, not that efficient though. And the serialized tree is compact.
Pre order traversal of BST will output root node first, then left children, then right.

root left1 left2 leftX right1 rightX
If we look at the value of the pre-order traversal we get this:

rootValue (<rootValue) (<rootValue) (<rootValue) |separate line| (>rootValue) (>rootValue)
Because of BST's property: before the |separate line| all the node values are less than root value, all the node values after |separate line| are greater than root value. We will utilize this to build left and right tree.

Pre-order traversal is BST's serialized string. I am doing it iteratively.
To deserialized it, use a queue to recursively get root node, left subtree and right subtree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            if not root: return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nums = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if nums and minVal < nums[0] < maxVal:
                front = nums.popleft()
                head = TreeNode(front)
                head.left = build(minVal, front)
                head.right = build(front, maxVal)
                return head

        return build(-float("inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))