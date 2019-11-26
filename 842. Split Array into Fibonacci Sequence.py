'''
842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
Accepted
14,166
Submissions
40,025

'''




'''
2019/11/25, python, backtracking

Runtime: 8 ms, faster than 28.67% of C++ online submissions for Split Array into Fibonacci Sequence.
Memory Usage: 9.5 MB, less than 100.00% of C++ online submissions for Split Array into Fibonacci Sequence.
Next challenges:


class Solution {
public:
    vector<int> splitIntoFibonacci(string S) {
        vector<int> res;
        backtracking(S, 0, res);
        return res;
        
    }
    
    bool backtracking(string s, int start, vector<int> &res){
        int n = s.size();
        if (start >= n && res.size() > 2) return true;
        int maxSplit = (s[start] == '0') ? 1: 10;
        for (int i = 1; i <= maxSplit && start + i <= s.size(); ++i){
            long long num = stoll(s.substr(start, i));
            if (num > INT_MAX) return false;
            int m = res.size();
            if (m >= 2 && (long long) res[m - 1] + (long long) res[m - 2] != num) continue;
            res.push_back(num);
            if(backtracking(s, start + i, res)) return true;
            res.pop_back();
        }
        return false;
    }
};
'''