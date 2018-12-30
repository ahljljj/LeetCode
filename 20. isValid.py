'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

# not my solution


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif stack:
                p = stack.pop()
                if p != c:
                    return False
        if stack:
            return False
        else:
            return True

# cpp, stack rewrite

'''
class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for (char ch: s){
            if (ch == '(' || ch == '[' || ch == '{')
                stack.push(ch);
            else if (ch == ')'){
                if (stack.empty() || stack.top() != '(') return false;
                else stack.pop();
            }
            else if (ch == ']'){
                if (stack.empty() || stack.top() != '[') return false;
                else stack.pop();
            }
            else if (ch == '}'){
                if (stack.empty() || stack.top() != '{') return false;
                else stack.pop();
            }
        }
        return stack.empty();
        
    }
};
'''