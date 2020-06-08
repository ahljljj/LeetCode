"""
307. Range Sum Query - Mutable


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.


"""

#segment tree


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n, 2 * self.n):
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, -1, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        pos = i + self.n
        self.tree[pos] = val
        while pos:
            parent = pos // 2
            if pos % 2 == 0:
                self.tree[parent] = self.tree[pos] + self.tree[pos + 1]
            else:
                self.tree[parent] = self.tree[pos] + self.tree[pos - 1]
            pos = parent

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        left = i + self.n
        right = j + self.n
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)



# 2020/05/07, binary indexed tree, too hard

'''
Runtime: 156 ms, faster than 79.38% of Python3 online submissions for Range Sum Query - Mutable.
Memory Usage: 17.9 MB, less than 33.33% of Python3 online submissions for Range Sum Query - Mutable.
'''


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (1 + self.n)
        if not nums:
            self.nums = []
            return
        self.nums = [0] * self.n
        for i in range(self.n):
            self.update(i, nums[i])

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        p = i + 1
        while p <= self.n:
            self.bit[p] += delta
            p += self.lowbit(p)

    def lowbit(self, x):
        return x & (-x)

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self.lowbit(i)
        return res

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum(j + 1) - self.prefix_sum(i)

# 2020/06/07, segment tree

'''
Runtime: 244 ms, faster than 67.28% of Python3 online submissions for Range Sum Query - Mutable.
Memory Usage: 23.1 MB, less than 11.68% of Python3 online submissions for Range Sum Query - Mutable.
'''


class NumArray:

    def __init__(self, nums: List[int]):
        self.root = SegmentTree.build(nums, 0, len(nums) - 1)

    def update(self, i: int, val: int) -> None:
        SegmentTree.modify(self.root, i, val)
        return

    def sumRange(self, i: int, j: int) -> int:
        return SegmentTree.query(self.root, i, j)


class SegmentTree:

    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None

    @classmethod
    def build(cls, nums, start, end):
        if start > end: return
        root = SegmentTree(start, end, nums[start])
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = cls.build(nums, start, mid)
        root.right = cls.build(nums, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    @classmethod
    def query(cls, root, start, end):
        if root.start == start and root.end == end:
            return root.sum
        mid = (root.start + root.end) // 2
        if end <= mid:
            return cls.query(root.left, start, end)
        if start > mid:
            return cls.query(root.right, start, end)
        l = cls.query(root.left, start, mid)
        r = cls.query(root.right, mid + 1, end)
        return l + r

    @classmethod
    def modify(cls, root, index, value):
        if not root: return
        if root.start == root.end:
            root.sum = value
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        root.sum = root.left.sum + root.right.sum
        return