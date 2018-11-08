"""
395. Longest Substring with At Least K Repeating Characters


Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.



"""

# recursion
# time complexity O(nlgn)??
# hard to analyze: t(n) = n + kt(n/k)

'''
i don't think the following is correct

I think the time complexity should be O(n^3) in worst case, notice there is substring() operation in while loop.
I guess amortized complexity should be O(n^2*logn) because if every time the divide character in the middle, call stack height will be log n and in each call stack, there will be O(n^2) operations.
Correct me if I'm wrong. Any suggestions?


'''

class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # edge case
        if not s: return 0
        # compute the frequency of each character
        dicts = {}
        for ch in s:
            dicts[ch] = dicts.get(ch, 0) + 1
        # if all characters have frequency return True
        flag = True
        for ch in s:
            if dicts[ch] < k:
                flag = False
                break
        if flag: return len(s)
       # otherwise we use all the infrequent elements as splits
        result = 0
        start, end = 0, 0
        while end < len(s):
            if dicts[s[end]] < k:
                result = max(result, self.longestSubstring(s[start: end], k))
                start = end + 1
            end += 1
        result = max(result, self.longestSubstring(s[start:], k)) # need do compare for the last segment
        return result

