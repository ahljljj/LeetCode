'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

#109 / 109 test cases passed. Runtime: 40 ms
#This running time beats 95.20% of python 3 submissions. May 2018

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        digits[-1]+=1
        i=n-1
        while i>=0:
            if digits[i]>=10 and i!=0:
                digits[i]=digits[i]%10
                digits[i-1]+=1
            elif digits[i]>=10 and i==0:
                digits[i]=digits[i]%10
                digits.insert(0,1)
            i-=1
        return digits