/*
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
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
    bool findTarget(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums);
        int l = 0, r = nums.size() - 1;
        while (l < r){
            int tmp = nums[l] + nums[r];
            if (tmp == k)
                return true;
            else if (tmp < k)
                ++l;
            else
                --r;
        }
        return false;

    }

    void inorder(TreeNode* root, vector<int> & nums){
        if (root == nullptr) return;
        inorder(root->left, nums);
        nums.push_back(root->val);
        inorder(root->right, nums);
    }
};

// cpp, dfs

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
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> s;
        return dfs(root, k, s);

    }

    bool dfs(TreeNode* root, int k, unordered_set<int> &s){
        if (!root) return false;
        if (s.find(k - root->val) != s.end()) return true;
        s.insert(root->val);
        return dfs(root->left, k, s) || dfs(root->right, k, s);
    }
};