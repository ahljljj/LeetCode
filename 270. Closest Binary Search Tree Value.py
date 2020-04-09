"""
270. Closest Binary Search Tree Value


Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4


"""

# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff, self.res = float("inf"), None
        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if not root:
            return
        curr = abs(root.val - target)
        if curr < self.diff:
            self.diff = curr
            self.res = root.val
        self.dfs(root.left, target)
        self.dfs(root.right, target)

# c++, dfs

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
    double diff = numeric_limits<double>::max(), res = NULL;
public:
    int closestValue(TreeNode* root, double target) {
        
        
        dfs(root, target);
        return res;
    }
    void dfs(TreeNode* root, double target){
        if(root == NULL) return;
        double curr = abs(root->val - target);
        if (curr < diff){
            diff = curr;
            res = root->val;
        }
        dfs(root->left, target);
        dfs(root->right, target);        
    }
};

'''

# modified cpp, dfs

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
public:
    int closestValue(TreeNode* root, double target) {
        int curr = root->val;
        auto kid = target < curr? root->left: root->right;
        if(! kid) return curr;
        int nxt = closestValue(kid, target);
        return abs(target - curr) < abs(target - nxt) ? curr : nxt;
        
    }
};

'''

# 2020/04/04, iterative

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float("inf")
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val
        return res

# divide and conquer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        low = self.low_bound(root, target)
        up = self.up_bound(root, target)
        if not low: return up.val
        if not up: return low.val
        if target - low.val < up.val - target: return low.val
        return up.val

    def low_bound(self, root, target):
        if not root: return root
        left = self.low_bound(root.left, target)
        right = self.low_bound(root.right, target)
        if target < root.val:
            return left
        return right if right else root

    def up_bound(self, root, target):
        if not root: return root
        left = self.up_bound(root.left, target)
        right = self.up_bound(root.right, target)
        if target > root.val:
            return self.up_bound(root.right, target)
        return left if left else root