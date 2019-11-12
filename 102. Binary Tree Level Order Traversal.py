"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        res = []

        queue = [root]

        while len(queue) > 0:
            res.append([node.val for node in queue])
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
        return res


# cpp, bfs, rewrite

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) return res;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()){
            int breadth = q.size();
            vector<int> tmp = {};
            for (int i = 0; i < breadth; ++i){
                TreeNode* curr = q.front(); q.pop();
                if (curr->left)q.push(curr->left);
                if(curr->right)q.push(curr->right);
                tmp.push_back(curr->val);
            }
            res.push_back(tmp);
        }
        return res;
        
        
    }
};

'''


'''
11/11/2019

Runtime: 48 ms, faster than 14.93% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
'''

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([root])
        while queue:
            breadth = len(queue)
            tmp = []
            for i in range(breadth):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
