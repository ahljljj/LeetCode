"""
62. Unique Paths


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


"""


# not my idea

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1] * m] * n

        for i in range(n):
            res[i][0] = 1
        for i in range(m):
            res[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[n - 1][m - 1]

# c++, dfs TLE

'''
class Solution {
public:
    int uniquePaths(int m, int n) {
        int res = 0; int s[2] = {0, 0};
        dfs(res, s, m, n);
        return res;
        
    }
    
    void dfs(int & res, int s[2], int m, int n){
        if (s[0] == m - 1 && s[1] == n- 1){
            ++res; return;
        }
        vector<vector<int>> dirs = {{1, 0}, {0, 1}};
        for (auto &dir: dirs){
            int x = s[0] + dir[0], y = s[1] + dir[1];
            int ns[2] = {x, y};
            if (x >= 0 && x < m && y >= 0 && y < n) dfs(res, ns, m, n);
        }
    }
};

'''

# c++, dynamic programmng, rewrite

'''
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i) dp[i][0] = 1;
        for (int j = 0; j < n; ++j) dp[0][j] = 1;
        for (int i = 1; i < m; ++i){
            for (int j = 1; j < n; ++j){
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
};
'''