"""
139. Word Break


Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false



"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        breakable = [False] * (len(s) + 1)
        breakable[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i + 1):
                if breakable[j] == True and (s[j: i] in wordDict):
                    breakable[i] = True
                    break

        return breakable[len(s)]

# cpp, dfs, tle

'''
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        return dfs(s, dict, 0);
        
    }
    
    bool dfs(string s, unordered_set<string> dict, int idx){
        if (idx == s.length()) return true;
        for (int i = idx; i < s.length(); ++i){
            string tmp = s.substr(idx, i - idx + 1);
            if (dict.find(tmp) != dict.end() && dfs(s, dict, i + 1)){
                return true;
            }
        }
        return false;
    }
};
'''

# cpp, dynamic programming

'''
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        vector<bool> dp( s.length(), false);
        for (int i = 0; i < s.length(); ++i){
            if (dict.find(s.substr(0, i + 1)) != dict.end()){
                dp[i] = true; 
            }
            for (int j = 0; j <= i; ++j){
                string tmp = s.substr(j + 1, i - j);
                if (dp[j] && dict.find(tmp) != dict.end()){
                    dp[i] = true;
                }
            }
        }
        return dp.back();
        
    }
};
'''


# 2020/04/15, memoization

'''
Runtime: 32 ms, faster than 89.85% of Python3 online submissions for Word Break.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Word Break.
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)
        self.dfs(s, wordDict, 0, memo)
        return memo[0]

    def dfs(self, source, wordDict, pos, memo):
        if pos in memo: return memo[pos]
        if pos == len(source):
            memo[pos] = True
            return True
        for i in range(pos, len(source)):
            prefix = source[pos: i + 1]
            if prefix not in wordDict: continue
            if self.dfs(source, wordDict, i + 1, memo):
                memo[pos] = True
                return memo[pos]
        memo[pos] = False
        return memo[pos]



