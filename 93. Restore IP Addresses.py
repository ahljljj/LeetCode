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
