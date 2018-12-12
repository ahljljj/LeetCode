"""
270. Closest Binary Search Tree Value


Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4


"""

# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff, self.res = float("inf"), None
        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if not root:
            return
        curr = abs(root.val - target)
        if curr < self.diff:
            self.diff = curr
            self.res = root.val
        self.dfs(root.left, target)
        self.dfs(root.right, target)

# c++, dfs

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
    double diff = numeric_limits<double>::max(), res = NULL;
public:
    int closestValue(TreeNode* root, double target) {
        
        
        dfs(root, target);
        return res;
    }
    void dfs(TreeNode* root, double target){
        if(root == NULL) return;
        double curr = abs(root->val - target);
        if (curr < diff){
            diff = curr;
            res = root->val;
        }
        dfs(root->left, target);
        dfs(root->right, target);        
    }
};

'''