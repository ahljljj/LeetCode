'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


#24ms 51.04%

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        for digit in digits:
            tmp = []
            for s in dp[digit]:
                if res:
                    for r in res:
                        tmp.append(r + s)
                else:
                    tmp.append(s)
            res = tmp
        return res

# cpp, rewtrite
'''
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return vector<string>();
        vector<string> table =  {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res = {""};
        for (char digit: digits){
            int idx = digit - '0' - 2;
            vector<string> tmp;
            for (char ch: table[idx]) {
                for (string s: res) tmp.push_back(s + ch);
            }
            res.swap(tmp);
        }
        return res;
        
    }
};

'''

'''
// cpp, backtracking

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return vector<string>();
        unordered_map<char, string> m = {{'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};
        vector<string> res; string tmp;
        dfs(digits, m, tmp, res, 0);
        return res;
        
    }
    
    void dfs(string digits, unordered_map<char, string> &m, string tmp, vector<string> &res, int idx){
        if (tmp.length() == digits.length()) {
            res.push_back(tmp);
            return;
        }
        for (int i = idx; i < digits.length(); ++i){
            for (auto s: m[digits[i]]) {
                tmp += s;
                dfs(digits, m, tmp, res, i + 1);
                tmp.pop_back();
            }
            
        }
        
    }
};

'''
