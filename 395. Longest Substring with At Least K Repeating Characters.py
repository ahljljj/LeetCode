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


# 2021/01/30, sliding window
# Runtime: 128 ms, faster than 41.72% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 14.4 MB, less than 68.66% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

# 循环sliding window
# 技巧性很强，不太容易能想到sliding window的方法
# 首先找出字符串中unique字符的个数
# 滑动窗口维护的是一个窗口中给定 unique 字符的一个窗口
# 如果window中的unique字符 > curr_unique，左移窗口；否则右移窗口

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_unique = set(s)
        ans = 0
        for curr_unique in range(1, len(max_unique) + 1):
            l, r = 0, 0
            count = 0
            curr_window = {}
            for r in range(len(s)):
                curr_window[s[r]] = curr_window.get(s[r], 0) + 1
                if curr_window[s[r]] == k:
                    count += 1
                while l <= r and len(curr_window) > curr_unique:
                    curr_window[s[l]] -= 1
                    if curr_window[s[l]] == k - 1:
                        count -= 1
                    if curr_window[s[l]] == 0:
                        curr_window.pop(s[l], None)
                    l += 1
                if count == curr_unique:
                    ans = max(ans, r - l + 1)
        return ans


# 2021/01/30, divide and conquer
# Runtime: 4180 ms, faster than 5.03% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 29.6 MB, less than 16.04% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.


# 挺难的，中点的选择很难想到

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.div_conq(s, 0, len(s) - 1, k)

    def div_conq(self, s, start, end, k):
        if end - start + 1 < k: return 0
        count = {}
        for i in range(start, end + 1):
            count[s[i]] = count.get(s[i], 0) + 1
        for m in range(start, end + 1):
            if count[s[m]] < k:
                return max(self.div_conq(s, start, m - 1, k), self.div_conq(s, m + 1, end, k))
        return end - start + 1

# 分治法稍微优化下，提升显著
# Runtime: 28 ms, faster than 95.86% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 14.2 MB, less than 86.22% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.div_conq(s, 0, len(s) - 1, k)

    def div_conq(self, s, start, end, k):
        if end - start + 1 < k: return 0
        count = {}
        for i in range(start, end + 1):
            count[s[i]] = count.get(s[i], 0) + 1
        for m in range(start, end + 1):
            if count[s[m]] < k:
                # start from m, find the maximal possible split point
                # save lots of time
                u = m
                while u <= end and count[s[u]] < k: u += 1
                return max(self.div_conq(s, start, m - 1, k), self.div_conq(s, u, end, k))
        return end - start + 1
