/*
508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.



*/

// cpp, two rounds search

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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        vector<int> nums;
        dfs(root, nums);
        unordered_map<int, int> m;
        for (int num: nums) ++m[num];
        int mostFreq = 0;
        for (auto itr = m.begin(); itr != m.end(); ++itr){
            mostFreq = max(mostFreq, itr->second);
        }
        vector<int> res;
        for (auto itr = m.begin(); itr != m.end(); ++itr){
            if (itr->second == mostFreq) res.push_back(itr->first);
        }
        return res;

    }

    int dfs(TreeNode * root, vector<int> & nums){
        if (root == nullptr) return 0;
        int sum = root->val;
        sum += dfs(root->left, nums) + dfs(root->right, nums);
        nums.push_back(sum);
        return sum;
    }
};