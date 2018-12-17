'''

298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

'''

# python, standard dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
A top down approach is similar to an in-order traversal. We use a variable length to store the current consecutive path length and pass it down the tree. As we traverse, we compare the current node with its parent node to determine if it is consecutive. If not, we reset the length.

Complexity analysis

Time complexity : O(n)O(n). The time complexity is the same as an in-order traversal of a binary tree with nn nodes.

Space complexity : O(n)O(n). The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to nn levels deep.

'''

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.dfs(root, None, 1)
        return self.res

    def dfs(self, root, prev, tmp):
        if not root:
            self.res = max(self.res, tmp)
            return
        if prev != None:
            if root.val == prev + 1:
                tmp += 1
            else:
                tmp = 1
            self.res = max(self.res, tmp)
        self.dfs(root.left, root.val, tmp)
        self.dfs(root.right, root.val, tmp)

# cpp, rewrite

'''
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
    int longestConsecutive(TreeNode* root) {
        if (!root) return 0;
        dfs(root, NULL, 1);
        return res;
        
    }
    
    void dfs(TreeNode* root, TreeNode* prev, int tmp){
        if (!root){
            res = max(res, tmp);
            return;
        }
        if (prev){
            if (root->val == prev->val + 1) 
                tmp += 1;
            else
                tmp = 1;
            res = max(res, tmp);
        }
        dfs(root->left, root, tmp);
        dfs(root->right, root, tmp);
    }
};

'''

# py, bottom up

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if root.left and root.val + 1 == root.left.val:
            l += 1
        else:
            l = 1
        if root.right and root.val + 1 == root.right.val:
            r += 1
        else:
            r = 1
        tmp = max(l, r)
        self.res = max(self.res, tmp)
        return tmp

