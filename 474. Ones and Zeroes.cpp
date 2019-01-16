/*
474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

*/

// cpp, brute force, tle

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int maxLen = 0;
        for (int i = 0; i < (1 << strs.size()); ++i){
            int currLen = 0, ones = 0, zeros = 0;
            for (int j = 0; j < strs.size(); ++j){
                if ((i & (1 << j)) != 0){
                    vector<int> tmp = counting(strs[j]);
//                    cout << tmp[0] << " " << tmp[1] << endl;
                    ones += tmp[1];
                    zeros += tmp[0];
                    ++currLen;
                }
            }
            if (zeros <= m && ones <= n) maxLen = max(maxLen, currLen);

        }
        return maxLen;

    }

    vector<int> counting(string & str){
        vector<int> res = {0, 0};
        for (int i = 0; i < str.size(); ++i) ++res[str[i] - '0'];
//        cout << res[0] << " " << res[1] << endl;
        return res;
    }
};


// cpp, recursion, brute force, tle

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        return dfs(strs, 0, m, n);

    }

    int dfs(vector<string> & strs, int idx, int m , int n){
        if (idx == strs.size()) return 0;
        vector<int> counts = counting(strs[idx]);
        int taken = -1;
        if (m - counts[0] >= 0 && n - counts[1] >= 0)
            taken = dfs(strs, idx + 1, m - counts[0], n - counts[1]) + 1;
        int not_taken = dfs(strs, idx + 1, m, n);
        return max(taken, not_taken);
    }

    vector<int> counting(string & str){
        vector<int> res = {0, 0};
        for (int i = 0; i < str.size(); ++i) ++res[str[i] - '0'];
        return res;
    }
};

// cpp, recursion with memo AC

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector< vector< vector<int> > > memo(strs.size(), vector<vector<int>>(m + 1, vector<int> (n + 1, 0)));
        return dfs(strs, 0, m, n, memo);

    }

    int dfs(vector<string> & strs, int idx, int m , int n, vector< vector< vector<int> > > & memo){
        if (idx == strs.size()) return 0;
        if (memo[idx][m][n] != 0) return memo[idx][m][n];
        vector<int> counts = counting(strs[idx]);
        int taken = -1;
        if (m - counts[0] >= 0 && n - counts[1] >= 0)
            taken = dfs(strs, idx + 1, m - counts[0], n - counts[1], memo) + 1;
        int not_taken = dfs(strs, idx + 1, m, n, memo);
        memo[idx][m][n] = max(taken, not_taken);
        return memo[idx][m][n];
    }

    vector<int> counting(string & str){
        vector<int> res = {0, 0};
        for (int i = 0; i < str.size(); ++i) ++res[str[i] - '0'];
        return res;
    }
};

// cpp, dynamic programming

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int dp[m + 1][n + 1];
        for (int i = 0; i < m + 1; ++i)
            for (int j = 0; j < n + 1; ++j)
                dp[i][j] = 0;
        for (string str: strs){
            int* counts = counting(str);
//            cout << counts[0] << " " << counts[1] << endl;
            for (int zeros = m; zeros >= counts[0]; --zeros)
                for (int ones = n; ones >= counts[1]; --ones)
                    dp[zeros][ones] = max(1 + dp[zeros - counts[0]][ones - counts[1]], dp[zeros][ones]);
        }
        return dp[m][n];

    }

    int* counting(string & str){
        int* res = new int[2]{0};
        for (int i = 0; i < str.size(); ++i) ++res[str[i] - '0'];
        return res;
    }
};