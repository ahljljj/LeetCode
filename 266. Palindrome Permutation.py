"""
266. Palindrome Permutation


Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true



"""


# hashtable

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hMap = {}
        for ch in s:
            if ch not in hMap:
                hMap[ch] = 1
            else:
                hMap[ch] += 1
        count = 0
        for (ch, freq) in hMap.items():
            if freq % 2:
                count += 1
            if count > 1:
                return False
        return True

# c++

'''
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> freq;
        for(auto ch : s) freq[ch]++;
        int res = 0;
        for (auto cnt: freq)
        {
            if (cnt.second % 2) res++;
            if (res > 1) return false;
        }
        return true;
        
    }
};


'''
