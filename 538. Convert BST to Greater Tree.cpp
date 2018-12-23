/*
538. Convert BST to Greater Tree



Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

*/

// cpp, dfs similar to inorder tranversal

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
    TreeNode* convertBST(TreeNode* root) {
        int prev = 0;
        dfs(root, prev);
        return root;
    }

    void dfs(TreeNode * & root, int & prev){
        if (!root) return;
        dfs(root->right, prev);
        if (prev) root->val += prev;
        prev = root->val;
        dfs(root->left, prev);
    }
};