'''
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Accepted
118,775
Submissions
289,318

'''


# 2020/05/07, binary indexed tree, not that good

'''
Runtime: 180 ms, faster than 41.64% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 17.7 MB, less than 37.50% of Python3 online submissions for Count of Smaller Numbers After Self.
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        bit = BITree(100000)
        for i in range(len(nums) - 1, -1, -1):
            res[i] = bit.prefix_sum(nums[i] + 1000)
            bit.update(nums[i] + 1000, 1)
        return res


class BITree:
    def __init__(self, n):
        self.bit = [0] * (1 + n)

    def update(self, i, val):
        i += 1
        while i < len(self.bit):
            self.bit[i] += val
            i += self.lowbit(i)

    def lowbit(self, x):
        return x & (-x)

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self.lowbit(i)
        return res

# 2020/06/08, segment tree, not that fast

'''
Runtime: 396 ms, faster than 12.28% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 19.5 MB, less than 5.77% of Python3 online submissions for Count of Smaller Numbers After Self.
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        min_val, max_val = min(nums), max(nums)
        root = SegmentTree.build(min_val, max_val)
        ans = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            SegmentTree.modify(root, nums[i], 1)
            ans[i] = SegmentTree.query(root, min_val, nums[i] - 1)
        return ans


class SegmentTree:

    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.left, self.right = None, None

    @classmethod
    def build(cls, start, end):
        if start > end:
            return
        root = SegmentTree(start, end, 0)
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = cls.build(start, mid)
        root.right = cls.build(mid + 1, end)
        return root

    @classmethod
    def modify(cls, root, index, value):
        if root.start == root.end:
            root.count += value
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        root.count = root.left.count + root.right.count
        return

    @classmethod
    def query(cls, root, start, end):
        if not root: return 0
        if start <= root.start and root.end <= end:
            return root.count
        mid = (root.start + root.end) // 2
        if end <= mid:
            return cls.query(root.left, start, end)
        if start > mid:
            return cls.query(root.right, start, end)
        l = cls.query(root.left, start, mid)
        r = cls.query(root.right, mid + 1, end)
        return l + r








