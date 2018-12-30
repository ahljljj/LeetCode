/*
617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.

*/

// cpp, modified original tree

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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        TreeNode* res = dfs(t1, t2);
        return res;

    }

    TreeNode* dfs(TreeNode* &t1, TreeNode* &t2){
//        TreeNode* res;
        if (t1 == nullptr) return t2;
        if (t2 == nullptr) return t1;
        t1->val = t1->val + t2->val;
        t1->left = dfs(t1->left, t2->left);
        t1->right = dfs(t1->right, t2->right);
        return t1;
    }

};

// cpp, not modify the original tree (mysterious)

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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        TreeNode* res = dfs(t1, t2);
        return res;

    }

    TreeNode* dfs(TreeNode* &t1, TreeNode* &t2){
//        if (t1 == nullptr && t2 == nullptr) return nullptr;
        if (t1 == nullptr) return t2;
        if (t2 == nullptr) return t1;
        TreeNode* res = new TreeNode(t1->val + t2->val);
//        res->val = t1->val + t2->val;
        res->left = dfs(t1->left, t2->left);
        res->right = dfs(t1->right, t2->right);
        return res;
    }

};