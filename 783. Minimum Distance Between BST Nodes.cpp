/*
783. Minimum Distance Between BST Nodes

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
*/

// cpp, inorder transversal

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
    int prev = INT_MAX, res = INT_MAX;
public:
    int minDiffInBST(TreeNode* root) {
        inorder(root);
        return res;

    }

    void inorder(TreeNode* root){
        if (root == nullptr) return;
        inorder(root->left);
        if (prev != INT_MAX) res = min(res, root->val - prev);
        prev = root->val;
        inorder(root->right);
    }
};