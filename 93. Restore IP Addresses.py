"""
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, res, [], 0)
        return res

    def helper(self, s, res, tmp, idx):
        if len(tmp) > 4: return
        if len(tmp) == 4 and idx == len(s):
            res.append('.'.join(tmp[:]))
            return
        for i in range(1, 4):
            if idx + i > len(s): break
            if int(s[idx: idx + i]) >= 256: continue
            if s[idx] == '0' and i > 1: continue
            tmp.append(s[idx: idx + i])
            self.helper(s, res, tmp, idx + i)
            tmp.pop()


# 2021/01/31
# Runtime: 32 ms, faster than 85.00% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 14.4 MB, less than 38.19% of Python3 online submissions for Restore IP Addresses.


# 全子集变形模板
# original 集合不是一个固定的集合
# 是从字符串start处开始的最长为3的一个子串，每次进入dfs时
# 有三种可能：s[start: start + i], i = 1, 2, 3
# 再剪枝掉不合格的子串即可


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, 0, ans, [])
        return ans

    def dfs(self, s, start, ans, subset):
        if len(subset) > 4: return
        if len(subset) == 4 and start == len(s):
            ans.append(".".join(subset))
            return
        for i in range(1, 4):
            if start >= len(s) or int(s[start: start + i]) > 255: continue
            if len(s[start: start + i]) > 1 and s[start: start + i].startswith("0"): continue
            subset.append(s[start: start + i])
            self.dfs(s, start + i, ans, subset)
            subset.pop()