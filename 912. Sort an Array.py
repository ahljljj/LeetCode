'''
912. Sort an Array

Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

2020/03/28, standard quick sort

Runtime: 584 ms, faster than 5.02% of Python3 online submissions for Sort an Array.
Memory Usage: 19.5 MB, less than 85.71% of Python3 online submissions for Sort an Array.


'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        if start >= end: return
        l, r = start, end
        m = (l + r) // 2
        target = nums[m]
        while l <= r:
            while l <= r and nums[l] < target:
                l += 1
            while l <= r and nums[r] > target:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1;
                r -= 1
        self.quick_sort(nums, start, r)
        self.quick_sort(nums, l, end)


# three pointers
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        if start >= end: return
        l, r = start, end
        m = (l + r) // 2
        target = nums[m]
        p = l
        while p <= r:
            if nums[p] > target:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
            elif nums[p] < target:
                nums[p], nums[l] = nums[l], nums[p]
                l += 1;
                p += 1
            else:
                p += 1
        self.quick_sort(nums, start, l)
        self.quick_sort(nums, p, end)

# merge sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1, [0] * len(nums))
        return nums

    def merge_sort(self, nums, l, r, tmp):
        if l >= r: return
        m = (l + r) // 2
        self.merge_sort(nums, l, m, tmp)
        self.merge_sort(nums, m + 1, r, tmp)
        self.merge(nums, l, m, r, tmp)

    def merge(self, nums, l, m, r, tmp):
        # two subarrays: [l, m] and [m + 1, r]
        # use tmp to record the tempory array
        i, j = l, m + 1
        p = l
        while i <= m and j <= r:
            if nums[i] < nums[j]:
                tmp[p] = nums[i]
                i += 1;
                p += 1
            else:
                tmp[p] = nums[j]
                j += 1;
                p += 1
        while i <= m:
            tmp[p] = nums[i]
            i += 1;
            p += 1
        while j <= r:
            tmp[p] = nums[j]
            j += 1;
            p += 1
        for x in range(l, r + 1):
            nums[x] = tmp[x]


# 2021/01/20, quick sort
# 双指针

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        k = nums[(start + end) >> 1]
        l, r = self.partition(nums, start, end, k)
        self.quick_sort(nums, start, l)
        self.quick_sort(nums, r, end)

    def partition(self, nums, start, end, k):
        l, r = start, end
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] > k:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1;
                r -= 1
        return r, l

# 2021/01/20， 三指针 quick sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        l, r = self.partition(nums, start, end, nums[(start + end) >> 1])
        self.quick_sort(nums, start, l)
        self.quick_sort(nums, r, end)
        return

    def partition(self, nums, start, end, k):
        l, r = start, end
        i = l
        while i <= r:
            if nums[i] > k:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] < k:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1;
                l += 1
            else:
                i += 1
        return l, i

# 2021/01/20, merge sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1, [None] * len(nums))
        return nums

    def merge_sort(self, nums, start, end, dummy):
        if start >= end: return
        m = (start + end) >> 1
        self.merge_sort(nums, start, m, dummy)
        self.merge_sort(nums, m + 1, end, dummy)
        self.merge(nums, start, m, end, dummy)

    def merge(self, nums, l, m, r, dummy):
        i, j = l, m + 1
        k = l
        while i <= m and j <= r:
            if nums[i] < nums[j]:
                dummy[k] = nums[i]
                i += 1;
                k += 1
            else:
                dummy[k] = nums[j]
                j += 1;
                k += 1
        while i <= m:
            dummy[k] = nums[i]
            k += 1;
            i += 1
        while j <= r:
            dummy[k] = nums[j]
            k += 1;
            j += 1
        for x in range(l, k):
            nums[x] = dummy[x]
