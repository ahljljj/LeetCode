/*
530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

*/

// cpp, inorder tranversal

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
    int getMinimumDifference(TreeNode* root) {
        int res = INT_MAX, prev = -1;
        dfs(root, res, prev);
        return res;

    }
    void dfs(TreeNode * root, int &res, int &prev){
        if (root == NULL) return;
        dfs(root->left, res, prev);
        if (prev != -1)
            res = min(res, abs(root->val - prev));
        prev = root->val;
        dfs(root->right, res, prev);
    }
};

// another

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
    int getMinimumDifference(TreeNode* root) {
        int res = INT_MAX;
        TreeNode * prev = new TreeNode(-1);
        dfs(root, res, prev);
        return res;

    }
    void dfs(TreeNode * root, int &res, TreeNode * &prev){
        if (root == NULL) return;
        dfs(root->left, res, prev);
        if (prev->val != -1)
            res = min(res, abs(root->val - prev->val));
        prev = root;
        dfs(root->right, res, prev);
    }
};