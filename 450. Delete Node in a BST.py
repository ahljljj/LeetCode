"""

450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

"""

#
'''

Steps:

Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
Once the node is found, have to handle the below 4 cases
node doesn't have left or right - return null
node only has left subtree- return the left subtree
node only has right subtree- return the right subtree
node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = self.findMin(root.right)
            root.val = node.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root


# iterative

'''
Find the node to be removed and its parent using binary search, and then use deleteRootNode to delete the root node of the subtree and return the new root node. This idea is taken from https://discuss.leetcode.com/topic/67309/an-easy-understanding-o-h-time-o-1-space-java-solution.

I'd also like to share my thinkings of the other solutions I've seen.

There are many solutions that got high votes using recursive approach, including the ones from the Princeton's Algorithm and Data Structure book. Don't you notice that recursive approach always takes extra space? Why not consider the iterative approach first?
Some solutions swap the values instead of swapping the nodes. In reality, the value of a node could be more complicated than just a single integer, so copying the contents might take much more time than just copying the reference.
As for the case when both children of the node to be deleted are not null, I transplant the successor to replace the node to be deleted, which is a bit harder to implement than just transplant the left subtree of the node to the left child of its successor. The former way is used in many text books too. Why? My guess is that transplanting the successor can keep the height of the tree almost unchanged, while transplanting the whole left subtree could increase the height and thus making the tree more unbalanced.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        curr = root  # target, the node with the key and which should be deleted
        prev = None
        while curr and curr.val != key:
            prev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not prev:
            return self.deleteRootNode(curr)
        if prev.left == curr:
            prev.left = self.deleteRootNode(curr)
        else:
            prev.right = self.deleteRootNode(curr)
        return root

    def deleteRootNode(self, root):
        # delete the target node and return the new root node
        if not root:
            return root
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            # minKid: the minimum node of the right subtree
        minKid = root.right
        # we need swap root and minKid
        # minKid is the new root
        while minKid and minKid.left:
            parent = minKid
            minKid = minKid.left
        minKid.left = root.left
        if minKid != root.right:
            parent.left = minKid.right
            minKid.right = root.right
        return minKid

# another iterative method, same idea

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        curr = root  # target, the node with the key and which should be deleted
        prev = None
        while curr and curr.val != key:
            prev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not prev:
            return self.deleteRootNode(curr)
        if prev.left == curr:
            prev.left = self.deleteRootNode(curr)
        else:
            prev.right = self.deleteRootNode(curr)
        return root

    def deleteRootNode(self, root):
        # delete the target node and return the new root node
        if not root:
            return root
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            # maxKid: the max node of the left subtree
        maxKid = root.left
        # we need swap root and maxKid
        # maxKid is the new root
        while maxKid and maxKid.right:
            parent = maxKid
            maxKid = maxKid.right
        maxKid.right = root.right
        if root.left != maxKid:
            parent.right = maxKid.left
            maxKid.left = root.left
        return maxKid


# 2020/04/04, divide and conquer? leetcode's solution

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.find_min(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.find_max(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root

    def find_min(self, root):
        while root.left: root = root.left
        return root.val

    def find_max(self, root):
        while root.right: root = root.right
        return root.val

# iterative implementation of the above algorithm

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root
        prev, target = self.find_node(root, key)
        if not target: return root
        if not prev:
            return self.delete_rootNode(target)
        if prev.left == target:
            prev.left = self.delete_rootNode(target)
        else:
            prev.right = self.delete_rootNode(target)
        return root

    def find_node(self, root, key):
        prev = None
        while root and root.val != key:
            prev = root
            if root.val < key:
                root = root.right
            else:
                root = root.left
        return prev, root

    def find_min(self, node):
        parent = None
        while node.left:
            parent = node
            node = node.left
        return parent, node

    def find_max(self, node):
        parent = None
        while node.right:
            parent = node
            node = node.right
        return parent, node

    def delete_rootNode(self, node):
        if not node.left and not node.right:
            return None
        elif node.right:
            parent, dummy = self.find_min(node.right)
            dummy.left = node.left
            if dummy != node.right:
                parent.left = dummy.right
                dummy.right = node.right
            return dummy
        else:
            parent, dummy = self.find_max(node.left)
            dummy.right = node.right
            if dummy != node.left:
                parent.right = dummy.left
                dummy.left = node.left
            return dummy





