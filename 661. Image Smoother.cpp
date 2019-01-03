/*
661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].


*/

// cpp, brute force

class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0 , -1}, {-1, -1}, {1, 1}, {-1, 1}, {1, -1}};
        int n = M.size(), m = M[0].size();
        vector<vector<int>> res(n, vector<int>(m));
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                int sum = M[i][j], count = 1;
                for (auto dir: dirs){
                    int ni = i + dir[0], nj = j + dir[1];
                    if (ni >=0 && ni < n && nj >= 0 && nj < m){
                        ++count; sum += M[ni][nj];
                    }
                }
                res[i][j] = sum / count;
            }
        }
        return res;

    }
};