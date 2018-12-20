/*
501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

*/

// cpp, dfs, map, and sort

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
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        map<int, int> m;
        dfs(root, m);
        vector<pair<int, int>> n;
        for(map<int,int>::iterator it = m.begin(); it != m.end(); ++it) n.push_back(make_pair(it->second, it->first));
        sort(n.begin(), n.end());
        for (int i = n.size() - 1; i > -1; --i){
            res.push_back(n[i].second);
            if (i > 0 && n[i - 1].first != n[i].first) break;
        }
        return res;
    }
    void dfs(TreeNode* root, map<int, int> &m){
        if (root == NULL) return;
        m[root->val] += 1;
        dfs(root->left, m);
        dfs(root->right, m);
    }
};