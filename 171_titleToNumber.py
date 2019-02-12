'''
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

'''

#1000 / 1000 test cases passed. Runtime: 28 ms 87.59%


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        num = 0
        i = 1
        for ss in s:
            num = (ord(ss) - ord('A') + 1) * i + num
            i = i * 26
        return num


# cpp, rewrite

'''
class Solution {
public:
    int titleToNumber(string s) {
        unordered_map<char, int> m;
        for(char c = 'A'; c <= 'Z'; ++c){
            m[c] = c - 'A' + 1;
        }
        int res = 0;
        for (char &c: s){
            res = res * 26 + m[c];
        }
        return res;
        
    }
};
'''
