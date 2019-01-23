/*
498. Diagonal Traverse


Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.

*/

// cpp, trick

/*

I don't think this is a hard problem. It is easy to figure out the walk pattern. Anyway...
Walk patterns:

If out of bottom border (row >= m) then row = m - 1; col += 2; change walk direction.
if out of right border (col >= n) then col = n - 1; row += 2; change walk direction.
if out of top border (row < 0) then row = 0; change walk direction.
if out of left border (col < 0) then col = 0; change walk direction.
Otherwise, just go along with the current direction.
Time complexity: O(m * n), m = number of rows, n = number of columns.
Space complexity: O(1).
*/

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};
        vector<int> res;
        int dirs[2][2] = {{-1, 1}, {1, -1}};
        int n = matrix.size(), m = matrix[0].size();
        int ni = 0, nj = 0, d = 0;
        for (int i = 0; i < n * m; ++i){
//            cout << matrix[ni][nj] << endl;
            res.push_back(matrix[ni][nj]);
            ni += dirs[d][0];
            nj += dirs[d][1];
            if (ni >= n) {ni = n - 1; nj += 2; d = 1 - d;}
            if (nj >= m) {nj = m - 1; ni += 2; d = 1 - d;}
            if (ni < 0){ni = 0; d = 1 - d;}
            if (nj < 0) {nj = 0; d = 1 - d;}

        }
        return res;
    }
};