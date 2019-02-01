'''
22. Generate Parentheses


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


'''

# not my idea

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

'''
//cpp, rewrite

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string tmp;
        dfs(res, tmp, n, 0, 0);
        return res;
        
    }
    void dfs (vector<string> &res, string tmp, int n, int l, int r){
        if (tmp.length() == 2*n) {
            res.push_back(tmp);
            return;
        }
        if (l < n) dfs(res, tmp + '(', n, l + 1, r);
        if (r < l) dfs(res, tmp + ')', n, l , r + 1);
        
    }
};

'''