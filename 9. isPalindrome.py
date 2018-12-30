'''

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

#11508 / 11508 test cases passed. Runtime: 304 ms
# This running time beats 58.97% of python3 submissions. May 2018

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        elif x<0 or x%10==0:
            return False
        x_r=0
        x_copy=x
        while x:
            if (x>=1 and x<=9):
                x_r+=x
            else:
                r=x%10
                x_r=(x_r+r)*10
            x=x//10
        if x_copy==x_r:
            return True
        else:
            return False

# cpp, rewrite

'''
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int res = 0, dummy = x;
        while (x){
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res == dummy;
        
    }
};

'''
