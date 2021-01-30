"""
241. Different Ways to Add Parentheses


Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


"""


class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for n1 in left:
                    for n2 in right:
                        res.append(self.helper(n1, n2, input[i]))
        return res

    def helper(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        else:
            return n1 * n2

# 2021/01/29
# Runtime: 32 ms, faster than 83.27% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 14.5 MB, less than 53.04% of Python3 online submissions for Different Ways to Add Parentheses.
# divide and conquer
# 很有技巧性的题目
# 利用for循环来找到运算符号+,-,*。以运算符号为中点将字符串分为左右两段
# 如果某段完全为整数，则直接返回，否则继续分治

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.div_conq(input, 0, len(input) - 1)

    def div_conq(self, inputs, start, end):
        if inputs[start: end + 1].isdigit():
            return [int(inputs[start: end + 1])]
        ans = []
        for i in range(start, end + 1):
            if inputs[i] == "+":
                left = self.div_conq(inputs, start, i - 1)
                right = self.div_conq(inputs, i + 1, end)
                ans.extend([x + y for x in left for y in right])
            elif inputs[i] == '-':
                left = self.div_conq(inputs, start, i - 1)
                right = self.div_conq(inputs, i + 1, end)
                ans.extend([x - y for x in left for y in right])
            elif inputs[i] == '*':
                left = self.div_conq(inputs, start, i - 1)
                right = self.div_conq(inputs, i + 1, end)
                ans.extend([x * y for x in left for y in right])
        return ans
