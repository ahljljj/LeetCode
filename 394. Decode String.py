"""
394. Decode String


Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


"""

# stack: iteration
# time complexity O(n)


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for ch in s:
            if not stack:
                if "0" < ch < "9":
                    stack.append(int(ch))
                else:
                    stack.append(ch)
                continue
            if "0" <= ch <= "9":
                if isinstance(stack[-1], int):
                    stack[-1] = stack[-1] * 10 + int(ch)
                else:
                    stack.append(int(ch))
            elif ch in letters:
                if isinstance(stack[-1], str) and stack[-1] != "[":
                    stack[-1] += ch
                else:
                    stack.append(ch)
            elif ch == "[":
                stack.append(ch)
            else:
                encoded = stack.pop()
                top = stack.pop()
                while top != "[":
                    encoded = top + encoded
                    top = stack.pop()
                num = stack.pop()
                stack.append(encoded * num)
        return "".join(stack)


# recursive

'''
intuition

Every time we meet a '[', we treat it as a subproblem so call our recursive function to get the content in that '[' and ']'. After that, repeat that content for 'num' times.
Every time we meet a ']', we know a subproblem finished and just return the 'word' we got in this subproblem.
Please notice that the 'pos' is passed by reference, use it to record the position of the original string we are looking at.


'''

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.pos = 0
        res = self.helper(s)
        return res

    def helper(self, s):
        num = 0
        word = ""
        while self.pos < len(s):
            curr = s[self.pos]
            if "0" <= curr <= "9":
                num = num * 10 + int(curr)
            elif curr == "[":
                self.pos += 1
                nextstr = self.helper(s)
                word += nextstr * num
                num = 0
            elif curr == "]":
                return word
            else:
                word += curr
            self.pos += 1
        return word


# 2020/06/16, dfs, rewrite, too clever

'''
Runtime: 20 ms, faster than 98.46% of Python3 online submissions for Decode String.
Memory Usage: 13.8 MB, less than 62.31% of Python3 online submissions for Decode String.
'''


class Solution:
    def decodeString(self, s: str) -> str:
        self.pos = 0
        return self.dfs(s)

    def dfs(self, s):
        word, num = "", 0
        while self.pos < len(s):
            c = s[self.pos]
            if c == ']':
                return word
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                word += c
            else:  # c == '['
                self.pos += 1
                next_word = self.dfs(s)
                word += next_word * num
                num = 0
            self.pos += 1
        return word



