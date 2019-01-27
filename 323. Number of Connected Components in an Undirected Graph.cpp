/*
323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

*/

// cpp, union find

/*
This is 1D version of Number of Islands II. For more explanations, check out this 2D Solution.

n points = n islands = n trees = n roots.
With each edge added, check which island is e[0] or e[1] belonging to.
If e[0] and e[1] are in same islands, do nothing.
Otherwise, union two islands, and reduce islands count by 1.
Bonus: path compression can reduce time by 50%.
Hope it helps!
*/

class Solution {
public:
    int countComponents(int n, vector<pair<int, int>>& edges) {
        vector<int> roots;
        for (int i = 0; i < n; ++i) roots.push_back(i);
        for (pair<int, int> p: edges){
            int p1 = find(roots, p.first);
            int p2 = find(roots, p.second);
            if (p1 != p2) {
                roots[p1] = p2;
                --n;
            }
        }
        return n;
    }

    int find(vector<int> roots, int node){
        while(roots[node] != node){
            roots[node] = roots[roots[node]];
            node = roots[node];
        }
        return node;
    }
};