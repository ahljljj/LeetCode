'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

''' running time error: 83 / 94 test cases passed.
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[]
        for i in range(len(s)-1):
            str=s[i]
            for s0 in s[i+1:len(s)]:
                if s0 in str:
                    s0_pos=str.find(s0)
                    str_temp=str[s0_pos:len(str)]+s0
                    if str_temp==str_temp[::-1]:
                        li.append(str_temp)
                str=str+s0
        max_num=1
        max_str=''
        for i in range(len(li)):
            if len(li[i])>max_num:
                max_num=len(li[i])
                max_str=li[i]
        if max_num>1:
            return max_str
        else:
            return s[0]
'''


# passed, not my idea

class Solution:
    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

# cpp, rewrite

'''
To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

We define P(i,j)P(i,j) as following:

P(i,j)={true,false,if the substring Si…Sj is a palindromeotherwise. 
Therefore,

P(i, j) = ( P(i+1, j-1) \text{ and } S_i == S_j )
P(i,j)=(P(i+1,j−1) and S 
i
​	
 ==S 
j
​	
 )

The base cases are:

P(i, i) = true
P(i,i)=true

P(i, i+1) = ( S_i == S_{i+1} )
P(i,i+1)=(S 
i
​	
 ==S 
i+1
​	
 )

This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...

'''


'''
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty() || s.length() == 1) return s;
        int maxLen = 1, start = 0;
        for (int i = 0; i < s.length(); ++i){
            int l = i, k = i;
            while (k < s.length() - 1 && s[k] == s[k + 1]) ++k; // skip the duplicates
            while (l > 0 && k < s.length() - 1 && s[l - 1] == s[k + 1]){
                --l; ++k;
            }
            int currLen = k - l + 1;
            if (currLen > maxLen){
                start = l;
                maxLen = currLen;
            }
        }
        return s.substr(start, maxLen);
        
    }
};

'''


'''
TLE, 2020/04/17, passed 102/103

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = None
        memo = {}
        self.dfs(s, 0, memo)
        #print(memo)
        return memo[0]
    
    def dfs(self, s, pos, memo):
        if not s:
            memo[pos] = ""
            return memo[pos]
        if pos in memo: return memo[pos]
        if pos == len(s): return ""
        curr = ""
        for i in range(pos, len(s)):
            prefix = s[pos: i + 1]
            if not self.is_valid(prefix): continue
            calculated =  self.dfs(s, i + 1, memo)
            max_sub = prefix if len(prefix) > len(calculated) else calculated
            curr = curr if len(curr) > len(max_sub) else max_sub
        memo[pos] = curr
        return memo[pos]
    
    def is_valid(self, s):
        return s == s[::-1]

'''