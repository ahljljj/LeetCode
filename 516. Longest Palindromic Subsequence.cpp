/*
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

*/

// cpp, dynamic programming

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        vector<vector<int>> dp = vector<vector<int>>(s.size(), vector<int>(s.size()));
        for (int i = s.size() - 1; i >= 0; --i){
            dp[i][i] = 1;
            for (int j = i + 1; j < s.size(); ++j){
                if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
                else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][s.size() - 1];

    }
};