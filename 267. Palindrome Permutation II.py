"""
267. Palindrome Permutation II


Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []



"""


# backtrack

class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        valid, hMap = self.isValid(s)
        if not valid: return []
        lHalf, mid = "", ""
        for ch, freq in hMap.items():
            if freq % 2: mid = ch
            lHalf += ch * (freq >> 1)
        res = []
        self.permute(res, lHalf, 0, mid)
        return res

    def isValid(self, s):
        hMap = {}
        valid = True
        res = 0
        for ch in s:
            hMap[ch] = hMap.get(ch, 0) + 1
        for ch, freq in hMap.items():
            if freq % 2: res += 1
            if res > 1:
                valid = False
                break
        return (valid, hMap)

    def permute(self, res, s, idx, mid):
        if idx == len(s):
            res.append(s + mid + s[::-1])
            return
        visited = set()
        for i in range(idx, len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if i == idx:
                    self.permute(res, s, idx + 1, mid)
                    continue
                s1, s2 = s[idx], s[i]
                s = s[:idx] + s2 + s[idx + 1: i] + s1 + s[i + 1:]
                self.permute(res, s, idx + 1, mid)
                s = s[:idx] + s1 + s[idx + 1: i] + s2 + s[i + 1:]





