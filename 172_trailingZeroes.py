'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

'''

'''
time limit exceeded

class Solution(object):
    def nfactor(self,n):
        n2=0
        n5=0
        m=n
        while m:
            if m%5==0:
                n5=n5+1
            else:
                break
            m=m//5
        m=n
        while m:
            if m%2==0:
                n2=n2+1
            else:
                break
            m=m//2
        return [n2,n5]
    
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        i=1
        n2=0
        n5=0
        while i<=n:
            if i%2==0:
                n2=n2+self.nfactor(i)[0]
            if i%5==0:
                n5=n5+self.nfactor(i)[1]
            i=i+1
        return min(n2,n5)
        
'''

# not my solution

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        num_zeros = 0
        pow_of_5 = 5

        while pow_of_5 <= n:
            num_zeros += n // pow_of_5
            pow_of_5 *= 5

        return num_zeros