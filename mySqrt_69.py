'''

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

'''time limit exceed
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        while i<=x:
            if i**2==x:
                return i
            elif i**2>x:
                return i-1
            i+=1
'''

# binary search
#1017 / 1017 test cases passed. Runtime: 84 ms
#This running time beats 27.06% of python 3 submissions. May 2018

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        while left<right:
            mid=left+(right-left)//2
            if mid**2==x:
                return mid
            elif mid**2>x:
                right=mid-1
            else:
                left=mid+1
        if left**2>x:
            return left-1
        else:
            return left


''' haven't verified
class Solution {
public:
    int mySqrt(long x) {
        for(long i=0; i<INT_MAX; i++){
            if(i*i <= x && x <(i+1)*(i+1)){
                return i;
            }
        }
        return -1;
    }
};
'''