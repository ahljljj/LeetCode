# 763. Partition Labels

# 2021/01/20, sliding window
# Runtime: 44 ms, faster than 40.63% of Python3 online submissions for Partition Labels.
# # Memory Usage: 14.3 MB, less than 27.54% of Python3 online submissions for Partition Labels.

# 注意：每次进入循环时update窗口的值，如果某个字符满了，delete掉这个key。当整个哈希表变为空的时候意味找到了一个串。重置左指针即可。


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        m = {}
        for ch in S:
            m[ch] = m.get(ch, 0) + 1
        l, r, curr = 0, 0, {}
        ans = []
        for r in range(len(S)):
            curr[S[r]] = curr.get(S[r], 0) + 1
            if curr[S[r]] == m[S[r]]:
                del curr[S[r]]
            if not curr:
                ans.append(r - l + 1)
                l = r + 1
        return ans

