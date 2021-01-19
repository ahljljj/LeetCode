# 1574. Shortest Subarray to be Removed to Make Array Sorted


# 2021/01/18, binary search, TLE
# 114 / 117 test cases passed.

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if self.check_validity(arr, m):
                r = m
            else:
                l = m
        # print(l, r)
        if self.check_validity(arr, l):
            return l
        return r

    def check_validity(self, nums, sub_arr_len):
        for i in range(len(nums) - sub_arr_len + 1):
            ordered = True
            for j in range(len(nums)):
                if j >= i and j < i + sub_arr_len:
                    continue
                if i > 0 and i + sub_arr_len < len(nums) and nums[i + sub_arr_len] < nums[i - 1]:
                    ordered = False
                    break
                if j > 0 and j != i + sub_arr_len and nums[j] < nums[j - 1]:
                    ordered = False
                    break
            if ordered: return True
        return False

# 2021/01/18, binary search, modify validity function

# Runtime: 1256 ms, faster than 5.09% of Python3 online submissions for Shortest Subarray to be Removed to Make Array Sorted.
# Memory Usage: 29.1 MB, less than 11.26% of Python3 online submissions for Shortest Subarray to be Removed to Make Array Sorted.


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        prefix, suffix = [1.0] * len(arr), [1.0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]: prefix[i] = prefix[i - 1] + 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= arr[i + 1]: suffix[i] = suffix[i + 1] + 1

        l, r = 0, len(arr) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if self.check_validity(arr, prefix, suffix, m):
                r = m
            else:
                l = m
        # print(l, r)
        if self.check_validity(arr, prefix, suffix, l):
            return l
        return r

    def check_validity(self, nums, prefix, suffix, sub_arr_len):
        for i in range(len(nums) - sub_arr_len + 1):
            # remove slice [i, i + sub_arr_len)
            left_num = nums[i - 1] if i > 0 else -float("inf")
            right_num = nums[i + sub_arr_len] if i + sub_arr_len < len(nums) else float("inf")
            left_prefix = prefix[i - 1] if i > 0 else 0
            right_suffix = suffix[i + sub_arr_len] if i + sub_arr_len < len(nums) else 0
            if left_num <= right_num and left_prefix + right_suffix == len(nums) - sub_arr_len:
                return True
        return False