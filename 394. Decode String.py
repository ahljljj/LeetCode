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

