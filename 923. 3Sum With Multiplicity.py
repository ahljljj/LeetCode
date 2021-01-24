# 923. 3Sum With Multiplicity

# 2021/01/23, two pointer
# 暴力解法通过了 O(n^2)

# Runtime: 4040 ms, faster than 5.22% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.5 MB, less than 21.64% of Python3 online submissions for 3Sum With Multiplicity.


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        arr = sorted(arr)
        for i in range(len(arr)):
            l, r = i + 1, len(arr) - 1
            curr = target - arr[i]
            count = 0
            while l < r:
                if arr[l] + arr[r] == curr:
                    if arr[l] != arr[r]:
                        count_l, count_r = 1, 1
                        while l + 1 < r and arr[l] == arr[l + 1]:
                            count_l += 1
                            l += 1
                        while r - 1 > l and arr[r] == arr[r - 1]:
                            count_r += 1
                            r -= 1
                        l += 1; r -= 1
                        ans += count_l * count_r
                    else:
                        ans += (r - l + 1) * (r - l) // 2
                        break
                elif arr[l] + arr[r] > curr:
                    r -= 1
                else:
                    l += 1
        return ans % (10 ** 9 + 7)