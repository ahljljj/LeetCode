# 1234. Replace the Substring for Balanced String

# 2021/01/24, sliding window

# Runtime: 188 ms, faster than 80.37% of Python3 online submissions for Replace the Substring for Balanced String.
# Memory Usage: 14.7 MB, less than 92.94% of Python3 online submissions for Replace the Substring for Balanced String.

# 滑动窗口技巧题
# 窗口外面四个元素的count <= 字符串长度的 1/4，则满足条件。这是因为窗口内部的元素可以任意改变
# 进入循环后，通过更新左端点来使得条件满足

class Solution:
    def balancedString(self, s: str) -> int:
        count = {}
        for ch in 'QWER':
            count[ch] = 0
        for ch in s:
            count[ch] += 1
        n = len(s) // 4
        ans = len(s)
        l = 0
        for r in range(len(s)):
            count[s[r]] -= 1
            while l < len(s) and count['Q'] <= n and count['W'] <= n \
                    and count['E'] <= n and count['R'] <= n:
                ans = min(ans, r - l + 1)
                count[s[l]] += 1
                l += 1
        return ans

