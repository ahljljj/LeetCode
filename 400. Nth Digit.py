"""
400. Nth Digit


Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


"""


# brute force: tle

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        res = 0
        for i in range(1, n + 1):
            tmp = str(i)
            for s in tmp:
                count += 1
                res = int(s)
                if count == n:
                    return res



# math

'''
intuition

To make the problem much much more easier, I divide the problem into 3 parts:

calculate how many digits the number has.
calculate what the number is.
find out which digit in the number is we wanted.
You can find the relative code part in the code section.
Here is an example to help you to understand my code:

Example:

Input: 250

After step 1, you will find that the 250th digit must belong to a 3-digit number, since 1~9 can only provide 9 digits and 10~99 can only provide 180 digits. Here, n = 250 - 9 - 90 * 2 = 61, and digits = 3.

In step 2, we will find the target number, which named as number in my code. From step 1, the n becomes to 61, which means "the 61st digit in 3-digit number is the digit we are looking for ." Easily, we know the 61st digit in 3-digit number belongs to number = 100 + 61 / 3 = 100 + 20 = 120. index is the index of the target digit in number. If index equals to 0, it means the target digit is the last digit of number.

Step 3, from step 2, we know index = n % digits = 61 % 3 = 1, which means the target digit is the 1st digit in number. Then, return 1.

'''


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits, base = 1, 9
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        r = n % digits
        q = n // digits
        tmp = 10 ** (digits - 1) + q - 1
        if r == 0:
            return tmp % 10
        reverse = 1 + digits - r
        nxt = tmp + 1
        for i in range(reverse):
            res = nxt % 10
            nxt //= 10
        return res
