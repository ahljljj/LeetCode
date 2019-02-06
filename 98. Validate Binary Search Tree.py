"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.


"""


'''
wrong

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        res = self.helper(root)
        return res if  res != None else True
    
    def helper(self, root):
        if not root: return
        if root.left and root.left.val >= root.val: return False
        if root.right and root.right.val <= root.val: return False
        self.helper(root.left)
        self.helper(root.right)

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, lower, upper):
        if not root: return True
        if not lower < root.val < upper: return False
        return self.helper(root.left, lower, root.val) and self.helper(root.right, root.val, upper)

# cpp, rewrite

'''
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return dfs(root, LONG_MIN, LONG_MAX);
    }
    
    bool dfs(TreeNode* root, long lower, long upper){
        if (root == nullptr) return true;
        if (root->val <= lower || root->val >= upper) return false;
        return dfs(root->left, lower, root->val) && dfs(root->right, root->val, upper);
    }
};

'''