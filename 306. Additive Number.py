"""
306. Additive Number


Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?



"""

#itertools
#Just trying all possibilities for the first two numbers and checking whether the rest fits.
#time complexity: O(n^2lgn), space complexity: O(n)

class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for (i, j) in itertools.combinations(range(1, n), 2):
            # length(first) cannot longer than half of the entire string length
            if i > n//2:
                break
            first, second = num[:i], num[i:j]
            # nums cannot startwith 0 unless the length is 0
            if first != str(int(first)) or second != str(int(second)):
                continue
            while j < n:
                third = str(int(first) + int(second))
                if num.startswith(third, j) == False:
                    break
                j += len(third)
                first, second = second, third
            if j == n:
                return True
        return False