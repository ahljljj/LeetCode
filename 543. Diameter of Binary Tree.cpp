/*
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


*/

// cpp, dfs, too slow

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
    int res = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == NULL) return 0;
        res = max(res, dfs(root->left) + dfs(root->right));
        diameterOfBinaryTree(root->left);
        diameterOfBinaryTree(root->right);
        return res;

    }

    int dfs (TreeNode * root){
        if (root == NULL) return 0;
        int left = 1 + dfs(root->left);
        int right = 1 + dfs(root->right);
        return max(left, right);
    }

};

// better cpp

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
    int res = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return res;

    }
    int depth(TreeNode * root){
        if (!root) return 0;
        int left = depth(root->left);
        int right = depth(root->right);
        res = max(res, left + right);
        return max(left, right) + 1;
    }
};


/*
2020/04/23, too complicated

Runtime: 44 ms, faster than 71.85% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15.7 MB, less than 58.62% of Python3 online submissions for Diameter of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        _, _, res = self.div_conq(root)
        return res

    def div_conq(self, root):
        if not root: return -1, -1, -1
        left_root_max, left_path_max, left_max = self.div_conq(root.left)
        right_root_max, right_path_max, right_max = self.div_conq(root.right)
        curr_root_max = 1 + max(left_root_max, right_root_max)
        curr_path_max = 2 + left_root_max + right_root_max
        curr_max = max([left_max, right_max, curr_path_max])
        return curr_root_max, curr_path_max, curr_max


*/