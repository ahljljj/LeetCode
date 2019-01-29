/*
333. Largest BST Subtree

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?

*/

// cpp, recursion

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct subTree{
    int size, lower, upper;
    subTree (int x, int l, int u): size(x), lower(l), upper(u){}
};

class Solution {
    int res = 0;
public:
    int largestBSTSubtree(TreeNode* root) {
        if (root == nullptr) return 0;
        traverse(root);
        return res;
    }

    subTree traverse(TreeNode* root){
        if (root == nullptr) return subTree(0, INT_MAX, INT_MIN);
        subTree l = traverse(root->left);
        subTree r = traverse(root->right);
        if (l.size == -1 || r.size == -1 || root->val <= l.upper || root->val >= r.lower)
            return subTree(-1, 0, 0);
        int tmp = l.size + 1 + r.size;
        res = max(res, tmp);
        return subTree(tmp, min(l.lower, root->val), max(r.upper, root->val));
    }
};