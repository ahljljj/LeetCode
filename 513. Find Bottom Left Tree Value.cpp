/*
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

*/

// cpp, breadth first search

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
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int res;
        while (!q.empty()){
            int breadth = q.size();
            TreeNode * first = q.front();
            res = first->val;
            for (int i = 0; i < breadth; ++i){
                TreeNode* tmp = q.front();
                q.pop();
                if (tmp->left)q.push(tmp->left);
                if (tmp->right)q.push(tmp->right);
            }
        }
        return res;

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
    int findBottomLeftValue(TreeNode* root) {
        int maxDepth = 0;
        int res = root->val;
        dfs(root, maxDepth, res, 0);
        return res;

    }

    void dfs (TreeNode* root, int &maxDepth, int &res, int depth){
        if (root == nullptr) return;
        if (depth > maxDepth){
            maxDepth = depth;
            res = root->val;
        }
        dfs(root->left, maxDepth, res, depth + 1);
        dfs(root->right, maxDepth, res, depth + 1);
    }
};


/*2020/04/22, bfs

Runtime: 44 ms, faster than 58.77% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.2 MB, less than 33.33% of Python3 online submissions for Find Bottom Left Tree Value.


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = collections.deque([root])
        res = None
        while q:
            size = len(q)
            for i in range(size):
                front = q.popleft()
                if i == 0: res = front.val
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
        return res


*/