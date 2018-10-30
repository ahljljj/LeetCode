"""
371. Sum of Two Integers


Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""

# python not work

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = a ^ b
        carry = (a & b) << 1
        while carry:
            tmp = res
            res = res ^ carry
            carry = (tmp & carry) << 1
        return res


# works on C++

'''

how does this work for negative integers?

let's try for a = 46, b = -14

46 = 101110
14 = 001110
-14 = 1's complement of (14) + 1 ( 1's complement = invert all bits)
so -14 = 110001
1 (+)
110010

so now all we have to do is add 46 and -14

46 = 101110
-14 = 110010 (+)
we get 100000 (which is 32 )

Note : we don't have to do the two's complement, the negative number will be already represented in two's complement.

class Solution {
public:
    int getSum(int a, int b) {
        
        int res {a ^ b}, carry {(a & b) << 1}, tmp;
        while (carry != 0){
            
            tmp = res;
            res = res ^ carry;
            carry = (tmp & carry) << 1;
            
        }
        return res;        
    }
};

'''