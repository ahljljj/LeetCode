'''
856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
Accepted
35,660
Submissions
59,664

'''

# 2020/06/18, stack

'''
Runtime: 28 ms, faster than 77.14% of Python3 online submissions for Score of Parentheses.
Memory Usage: 13.8 MB, less than 64.26% of Python3 online submissions for Score of Parentheses.

'''


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                ans = 0
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                if stack: stack.pop()
                stack.append(ans * 2 if ans else 1)
        return sum(stack)
