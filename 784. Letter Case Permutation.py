# 784. Letter Case Permutation


# 2021/01/31
# Runtime: 92 ms, faster than 18.70% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 14.8 MB, less than 78.22% of Python3 online submissions for Letter Case Permutation.


# 全子集标准模板
# 如果遇到小写字符，则变为大写
# 如果遇到大写字条，则变为小写
# 如果遇到数字，continue

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        self.dfs(S, 0, ans)
        return ans

    def dfs(self, s, start, ans):
        ans.append(s)
        for i in range(start, len(s)):
            if 'a' <= s[i] <= 'z':
                self.dfs(s[: i] + s[i].upper() + s[i + 1:], i + 1, ans)
            if 'A' <= s[i] <= 'Z':
                self.dfs(s[: i] + s[i].lower() + s[i + 1:], i + 1, ans)