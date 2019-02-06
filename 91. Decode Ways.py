"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""


'''
wrong

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0
        count = 0
        n = len(s)
        for i in range(n):
            if i == 0:
                count += 1
                continue
            if s[i] == '0':
                if int(s[i-1]) > 2 or int(s[i-1]) == 0:
                    return 0
                else:
                    continue

            tmp = s[i-1]+s[i]
            if 0< int(tmp) <= 26 and s[i] != '0' and s[i-1] != '0': count += 1
        return count
            
            
        

'''


class Solution:

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        counts = [0] * n
        counts[0] = 1 if s[0] != '0' else 0

        for i in range(1, n):
            if i == 1:
                if 1 <= int(s[1]) <= 9:
                    counts[1] += counts[0]
                if 10 <= int(s[0] + s[1]) <= 26:
                    counts[1] += 1
            else:
                if 1 <= int(s[i]) <= 9:
                    counts[i] = counts[i - 1]
                if 10 <= int(s[i - 1] + s[i]) <= 26:
                    counts[i] += counts[i - 2]
        return counts[n - 1]

# cpp, dynamic programming, rewrite

'''
class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0') return 0;
        vector<int> dp(s.size() + 1);
        dp[0] = 1; dp[1] = 1;
        for (int i = 2; i <= s.size(); ++i){
            if (s[i - 1] != '0') dp[i] += dp[i - 1];
            if (s[i - 2] != '0' && stoi(s.substr(i - 2, 2))  <= 26) dp[i] += dp[i - 2];
        }
        return dp.back();
        
    }
};
'''