/*
590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:







Return its postorder traversal as: [5,6,3,2,4,1].


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
    vector<int> postorder(Node* root) {
        dfs(root);
        return res;

    }

    void dfs(Node* root){
        if (root == nullptr) return;
        for (auto node: root->children) dfs(node);
        res.push_back(root->val);
    }
};