'''
294. Flip Game II

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.


'''

# cpp, backtracking (brute force)

'''
class Solution {
public:
    bool canWin(string s) {
        if (s.size() < 2) return false;
        for (int i = 0; i < s.size() - 1; i++){
            if (s.substr(i, 2) == "++"){
                s[i] = '-'; s[i + 1] = '-';
                if (not canWin(s))return true;
                s[i] = '+'; s[i + 1] = '+';
            }
        }
        return false;
    }
};

'''

# py AC, brute force with memorization

class Solution:
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.memo = {}
        return self.dfs(s)

    def dfs(self, s):
        if len(s) < 2: return False
        if s in self.memo:
            return not self.memo[s]
        for i in range(len(s) - 1):
            if s[i: i + 2] == "++":
                s = s[:i] + "--" + s[i + 2:]
                if s in self.memo and not self.memo[s]:
                    return True
                if not self.dfs(s):
                    self.memo[s] = True
                    return True
                s = s[:i] + "++" + s[i + 2:]
        self.memo[s] = False
        return False


# 2021/01/31
# backtracking, no memo
# Runtime: 1108 ms, faster than 18.71% of Python3 online submissions for Flip Game II.
# Memory Usage: 14.1 MB, less than 93.23% of Python3 online submissions for Flip Game II.

# canWin函数的是这个player能否找到一条必胜策略的可能性。并不意味着player一定能赢。

class Solution:
    def canWin(self, s: str) -> bool:
        s = list(s)
        return self.dfs(s)

    def dfs(self, s):
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                s[i] = '-';
                s[i + 1] = '-'
                if not self.canWin(s): return True
                s[i] = '+';
                s[i + 1] = '+'
        return False