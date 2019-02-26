"""
227. Basic Calculator II


Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.


"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        i = 0
        tmp, i = self.nextint(s, 0)
        stack.append(tmp)
        while i < len(s):
            op = s[i]
            tmp, i = self.nextint(s, i + 1)
            if op == '+': stack.append(tmp)
            if op == '-': stack.append(-tmp)
            if op == '*': stack[-1] *= tmp
            if op == '/': stack[-1] = stack[-1] / tmp if stack[-1] >= 0 else -(-stack[-1] / tmp)
        return sum(stack)

    def nextint(self, s, i):
        res = 0
        while i < len(s) and s[i] not in '+-*/':
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        return (res, i)


# cpp, rewrite

'''
class Solution {
public:
    int calculate(string s) {
        stack<int> stk;
        long num = 0;
        char sign = '+';
        for (int i = 0; i < s.size(); ++i){
            char ch = s[i];
            if (ch >= '0' && ch <= '9'){
                num = num * 10 + ch - '0';
            } 
            if (((ch < '0' || ch > '9') && ch != ' ') || i == s.size() - 1){
                if (sign == '-') stk.push(-num);
                else if (sign == '+') stk.push(num);
                else if (sign == '*'){
                    long tmp = stk.top();
                    tmp *= num;
                    stk.pop(); stk.push(tmp);                    
                }else if (sign == '/'){
                    long tmp = stk.top();
                    tmp /= num;
                    stk.pop(); stk.push(tmp);
                }
                num = 0;
                sign = ch;
            }            
        }
        int res = 0;
        while (!stk.empty()){
            int curr = stk.top();
            res += curr;
            stk.pop();
        }
        return res;
        
    }
};
'''

