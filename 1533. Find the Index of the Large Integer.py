# 1533. Find the Index of the Large Integer

# 2021/01/18, binary search
# 对奇偶长度分开来讨论。偶数时没有问题，奇数时需要把中间那个元素回到后半部分


# Runtime: 244 ms, faster than 98.98% of Python3 online submissions for Find the Index of the Large Integer.
# Memory Usage: 53.6 MB, less than 57.14% of Python3 online submissions for Find the Index of the Large Integer.

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if (r - l) % 2:
                if reader.compareSub(l, m, m + 1, r) > 0:
                    r = m
                else:
                    l = m + 1
            else:
                if reader.compareSub(l, m, m, r) > 0:
                    r = m
                else:
                    l = m
        if reader.compareSub(l, l, r, r) > 0:
            return l
        return r
