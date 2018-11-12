"""
402. Remove K Digits


Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.



"""


# try hard by doing this in one pass, but failed

'''
# wrong


class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"        
        res = ""
        n = len(num)
        start = 0
        for i in range(1, n):
            if int(num[i]) < int(num[i - 1]):
                res += num[start : i - 1]
                start = i
                k -= 1
            if k == 0:
                res += num[start:]
                break
#            if k == n - i:
#                res += num[start : i]
#                break
            
        print(start, k)
        res += num[start : n - k]

#        return res
        i = 0
        while i < len(res) and res[i] == "0":
            i += 1
        return res[i:] if i < len(res) else "0"
'''


# solve this in multiple pass
# time complexity O(kn)
'''
intuition

The first algorithm is straight-forward. Let's think about the simplest case: how to remove 1 digit from the number so that the new number is the smallest possible？ Well, one can simply scan from left to right, and remove the first "peak" digit; the peak digit is larger than its right neighbor. One can repeat this procedure k times, and obtain the first algorithm:


'''

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        while k > 0:
            i = 0
            while i < len(num) - 1 and num[i] <= num[i + 1]:
                i += 1
            if i == len(num) - 1:
                num = num[:-1]
            else:
                num = num[:i] + num[i + 1:]
            k -= 1
        i = 0
        while i < len(num) and num[i] == "0":
            i += 1
        return num[i:] if i < len(num) else "0"

# stack

'''
intuition

The above algorithm is a bit inefficient because it frequently remove a particular element from a string and has complexity O(k*n).

One can simulate the above procedure by using a stack, and obtain a O(n) algorithm. Note, when the result stack (i.e. res) pop a digit, it is equivalent as remove that "peak" digit.


'''

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        stack = []
        keep = len(num) - k
        for i in range(len(num)):
            while stack and k > 0 and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        stack = stack[:keep]

        # trim leading zeros
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        return "".join(stack[i:]) if i < len(stack) else "0"




