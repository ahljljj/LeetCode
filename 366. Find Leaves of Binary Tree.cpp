/*
366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []


*/

// cpp, dfs

/*
For this question we need to take bottom-up approach. The key is to find the height of each node. Here the definition of height is:
The height of a node is the number of edges from the node to the deepest leaf. --CMU 15-121 Binary Trees

I used a helper function to return the height of current node. According to the definition, the height of leaf is 0. h(node) = 1 + max(h(node.left), h(node.right)).
The height of a node is also the its index in the result list (res). For example, leaves, whose heights are 0, are stored in res[0]. Once we find the height of a node, we can put it directly into the result.

UPDATE:
Thanks @adrianliu0729 for pointing out that my previous code does not actually remove leaves. I added one line node.left = node.right = null; to remove visited nodes

UPDATE:
There seems to be some debate over whether we need to actually "remove" leaves from the input tree. Anyway, it is just a matter of one line code. In the actual interview, just confirm with the interviewer whether removal is required.
*/


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
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> res;
        height(root, res);
        return res;

    }

    int height(TreeNode*root, vector<vector<int>> &res){
        if (root == nullptr) return -1;
        int h = 1 + max(height(root->left, res), height(root->right, res));
        if (res.size() < h + 1) res.push_back({root->val});
        else
            res[h].push_back(root->val);
        return h;
    }
};


/*
2020/04/17, divide and conquer

Runtime: 32 ms, faster than 36.17% of Python3 online submissions for Find Leaves of Binary Tree.
Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for Find Leaves of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        memo= {}
        res = []
        self.dfs(root, memo)
        for i in range(len(memo)):
            res.append(memo[i])
        return res

    def dfs(self, root, memo):
        if not root: return -1
        if not root.left and not root.right:
            if 0 not in memo:
                memo[0] = [root.val]
            else:
                memo[0].append(root.val)
            return 0
        left = self.dfs(root.left, memo)
        right = self.dfs(root.right, memo)
        height = 1 + max(left, right)
        if height not in memo:
            memo[height] = [root.val]
        else:
            memo[height].append(root.val)
        return height


*/