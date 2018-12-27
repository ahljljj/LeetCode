/*
589. N-ary Tree Preorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:







Return its preorder traversal as: [1,3,5,6,2,4].



Note:

Recursive solution is trivial, could you do it iteratively?

*/

// cpp, standard dfs

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    vector<int> res;
public:
    vector<int> preorder(Node* root) {
        dfs(root);
        return res;

    }
    void dfs(Node* root){
        if (root == nullptr) return;
        res.push_back(root->val);
        for(auto node : root->children) dfs(node);
    }
};