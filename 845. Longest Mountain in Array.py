# 845. Longest Mountain in Array


# 2021/01/21， two pointer

# Runtime: 184 ms, faster than 24.25% of Python3 online submissions for Longest Mountain in Array.
# Memory Usage: 15.2 MB, less than 82.53% of Python3 online submissions for Longest Mountain in Array.

# 技巧性很强
# 不一样的双指针。进入循环后，通过更新右指针来找到一个合适的mountain
# 不管有没有找到mountain都会更新左指针。

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        while l < len(arr):
            r = l
            if r + 1 < len(arr) and arr[r] < arr[r + 1]:
                while r + 1 < len(arr) and arr[r] < arr[r + 1]:
                    r += 1
                if r + 1 == len(arr): break
                while r + 1 < len(arr) and arr[r] > arr[r + 1]:
                    r += 1
                if arr[r] < arr[r - 1]:
                    ans = max(ans, r - l + 1)
            l = max(r, l + 1)
        return ans
