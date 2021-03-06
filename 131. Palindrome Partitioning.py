"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]


"""

'''
time limit exceeded


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(res, [], s, 0)
        return res

    def is_valid(self, s):
        return s == s[::-1]

    def helper(self, res, tmp, s, idx):
        if idx == len(s)  and ''.join(tmp) == s:
            res.append(tmp[:])
            return
        for i in range(idx, len(s)):
            for j in range(len(s) - i):
                if self.is_valid(s[i: i + j + 1]):
                    tmp.append(s[i: i + j + 1])
                    self.helper(res, tmp, s, i + j + 1)
                    tmp.pop()
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(res, [], s)
        return res

    def is_valid(self, s):
        return s == s[::-1]

    def helper(self, res, tmp, s):
        if not s:
            res.append(tmp[:])
            return
        for i in range(1, len(s) + 1):
            if self.is_valid(s[:i]):
                tmp.append(s[:i])
                self.helper(res, tmp, s[i:])
                tmp.pop()

# cpp, backtracking, rewrite

'''
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> tmp = {};
        dfs(res, tmp, s, 0);
        return res;
        
    }
    
    bool valid(string s){
        int l = 0, r = s.length() - 1;
        while (l < r){
            if (s[l] != s[r]) return false;
            ++l; --r;
        }
        return true;
    }
    void dfs(vector<vector<string>> &res, vector<string> tmp, string s, int idx){
        if (s.length() == idx) res.push_back(tmp);
        for (int i = idx; i < s.length(); ++i){
            if (!valid(s.substr(idx, i - idx + 1)))
                continue;
            tmp.push_back(s.substr(idx, i - idx + 1));
            dfs(res, tmp, s, i + 1);
            tmp.pop_back();
        }
    }
};
'''


# 2020/04/14, subset

'''
Runtime: 92 ms, faster than 25.94% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Palindrome Partitioning.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, res, [], 0)
        return res

    def dfs(self, s, res, subset, pos):
        if not s: return
        if pos == len(s):
            res.append(subset[:])
        for i in range(pos, len(s)):
            prefix = s[pos: i + 1]
            if not self.is_valid(prefix): continue
            subset.append(prefix)
            self.dfs(s, res, subset, i + 1)
            subset.pop()

    def is_valid(self, s):
        return s == s[::-1]

# 2020/04/15, memoization

'''
Runtime: 60 ms, faster than 95.31% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 16.1 MB, less than 5.88% of Python3 online submissions for Palindrome Partitioning.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, memo = [], {}
        return self.dfs(s, res, 0, memo)

    def dfs(self, s, res, pos, memo):
        if not s: return []
        if pos == len(s):
            memo[pos] = [[]]
            return memo[pos]
        if pos in memo: return memo[pos]
        subset = []
        for i in range(pos, len(s)):
            prefix = s[pos: i + 1]
            if not self.is_valid(prefix): continue
            sub_partitions = self.dfs(s, res, i + 1, memo)
            for par in sub_partitions:
                subset.append([prefix] + par)
        memo[pos] = subset
        return memo[pos]

    def is_valid(self, s):
        return s == s[::-1]