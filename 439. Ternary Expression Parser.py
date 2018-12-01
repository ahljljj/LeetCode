"""
439. Ternary Expression Parser


Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).

Note:

The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
Example 1:

Input: "T?2:3"

Output: "2"

Explanation: If true, then result is 2; otherwise result is 3.
Example 2:

Input: "F?1:T?4:5"

Output: "4"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Example 3:

Input: "T?T?F:5:3"

Output: "F"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"


"""

'''
wrong 

class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        return self.dfs(expression)
        
    def dfs(self, expression):
        if expression.isdigit() or len(expression) == 1:
            return expression
        if expression[0] == 'T':
            l = 2
            if expression[l] in 'TF':
                r = len(expression) - 1
                while expression[r] != ':':
                    r -= 1
            else:
                r = l
                while expression[r] != ':':
                    r += 1
            return self.dfs(expression[l : r])
        else: # expression[0] == 'F'
            l = 2
            if l < len(expression) and expression[l] in 'TF':
                r = len(expression) - 1
                while expression[r] != ':':
                    r -= 1
                return self.dfs(expression[r + 1 : ])
            else:
                while l < len(expression) and expression[l] != ':':
                    l += 1
                return self.dfs(expression[l + 1: ])
            
            
        

'''

# stack
'''
Iterate the expression from tail, whenever encounter a character before '?', calculate the right value and push back to stack.

P.S. this code is guaranteed only if "the given expression is valid" base on the requirement.

'''


class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for s in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()
                if s == 'T':
                    top = stack.pop()
                    stack.pop()
                    stack.append(top)
                else:
                    stack.pop()
                continue
            if s != ':':
                stack.append(s)
        return stack[0]
