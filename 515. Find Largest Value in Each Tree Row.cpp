/*
515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

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
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) return {};
        queue<TreeNode*> q;
        q.push(root);
        vector<int> res;
        while(!q.empty()){
            int breadth = q.size();
            int currMax = INT_MIN;
            for (int i = 0; i < breadth; ++i){
                TreeNode* tmp = q.front();
                q.pop();
                currMax = max(currMax, tmp->val);
                if(tmp->left) q.push(tmp->left);
                if(tmp->right) q.push(tmp->right);
            }
            res.push_back(currMax);
        }
        return res;
    }
};


/*
2020/04/23, bfs, simple

Runtime: 48 ms, faster than 59.09% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 15.9 MB, less than 20.00% of Python3 online submissions for Find Largest Value in Each Tree Row.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = collections.deque([root])
        res = []
        while q:
            size = len(q)
            max_val = -float("inf")
            for _ in range(size):
                front = q.popleft()
                max_val = max(max_val, front.val)
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            res.append(max_val)
        return res




*/