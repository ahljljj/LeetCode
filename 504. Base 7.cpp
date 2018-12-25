/*
504. Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

*/

// cpp, brute force

class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0) return "0";
        string res, sign = num < 0? "-" :"";
        num = abs(num);
        while (num){
            int r = num % 7;
            res = to_string(r) + res;
            num /= 7;
        }
        res = sign + res;



        return res;
    }
};

// cpp, standard bfs

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
public:
    int maxDepth(Node* root) {
        if (root == nullptr) return 0;
        queue<Node*> q; q.push(root);
        int depth = 0;
        while (! q.empty()){
            ++depth;
            int currSize = q.size();
            for(int i = 0; i < currSize; ++i){
                Node * curr = q.front(); q.pop();
                for (auto kid: curr->children) q.push(kid);
            }
        }
        return depth;

    }
};