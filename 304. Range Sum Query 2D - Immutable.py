"""
304. Range Sum Query 2D - Immutable


Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.


"""

'''
# c++ codes


class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        int n = matrix.size();
        int m = n > 0? matrix[0].size(): 0;
        sum = vector<vector<int>>(1 + n, vector<int>(1 + m, 0));
        for (int i = 1; i <= n; i++)
            for(int j = 1; j <= m; j++){
             sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + matrix[i - 1][j - 1];    
            }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {

        return sum[row2 + 1][col2 + 1] - sum[row1][col2 + 1] - sum[row2 + 1][col1] + sum[row1][col1];
        
    }
private:
    vector<vector<int>> sum;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
'''


# 2020/05/06, dynamic programming

'''
Runtime: 116 ms, faster than 63.76% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 16.9 MB, less than 16.67% of Python3 online submissions for Range Sum Query 2D - Immutable.
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.dp = [[0]]
            return
        n, m = len(matrix), len(matrix[0])
        self.dp = [[0] * (1 + m) for _ in range(1 + n)]
        for i in range(n):
            for j in range(m):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + self.dp[i][j + 1] \
                                        - self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] \
               - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] \
               + self.dp[row1][col1]