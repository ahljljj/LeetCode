/*
541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

*/

// cpp, module, brute force

class Solution {
public:
    string reverseStr(string s, int k) {
        int tail = s.length() % (2*k);
        for (int i = 0; i < s.length() - tail; i += 2*k)
            reverse(s, i, k);
        if (tail <= k )
            reverse(s, s.length() - tail, tail);
        else
            reverse(s, s.length() - tail, k);
        return s;
    }

    void reverse(string &s, int start, int length){
        int left = start, right = start + length - 1;
        while (left < right){
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            ++left; --right;
        }
    }
};