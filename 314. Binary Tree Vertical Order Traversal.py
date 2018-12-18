"""
314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

"""

# python, hash table

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        this problem seemed very hard but actually once you draw a picture on a paper or in your brain, it becomes pretty clear.
        - for the left  node, you set its index as index - 1
        - for the right node, you set its index as index + 1
        - use queue to loop through all the nodes in a tree
        - set index as a key to the hashmap() and value as a list of vals
        - add node.data into hashmap() with index as a key
        - keep track of min and max index and store into solution list and return it
        """
        if not root: return []
        table = {}
        queue = collections.deque([(root, 0)])
        minIdx, maxIdx = 0, 0
        while queue:
            node, idx = queue.popleft()
            if idx not in table:
                table[idx] = [node.val]
            else:
                table[idx].append(node.val)
            if node.left:
                minIdx = min(minIdx, idx - 1)
                queue.append((node.left, idx - 1))
            if node.right:
                maxIdx = max(maxIdx, idx + 1)
                queue.append((node.right, idx + 1))
        res = []
        for i in range(minIdx, maxIdx + 1):
            res.append(table[i])
        return res

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
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<pair<TreeNode*, int>> q;
        q.push(make_pair(root, 0));
        int minIdx = 0, maxIdx = 0;
        unordered_map<int, vector<int> > table;
        while (!q.empty()){
            TreeNode* node = q.front().first;
            int idx = q.front().second;
            q.pop();
            table[idx].push_back(node->val);
            if (node->left){
                minIdx = min(minIdx, idx - 1);
                q.push(make_pair(node->left, idx - 1));
            }
            if (node->right){
                maxIdx = max(maxIdx, idx + 1);
                q.push(make_pair(node->right, idx + 1));
            }            
        }
        for (int i = minIdx; i <= maxIdx; ++i) res.push_back(table[i]);
        return res;
        
        
    }
};

'''