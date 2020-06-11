'''

480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.

'''

# 2020/06/10, two heaps

'''
Runtime: 276 ms, faster than 51.34% of Python3 online submissions for Sliding Window Median.
Memory Usage: 15.7 MB, less than 32.37% of Python3 online submissions for Sliding Window Median.
'''


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        # min_heap: large nums
        # max_heap: small nums
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        max_heap = []
        half = k // 2 + 1 if k & 1 else k // 2
        for i in range(half):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        ans.append(self.get_median(max_heap, min_heap, k))
        to_be_deleted = collections.defaultdict(int)
        for r in range(k, len(nums)):
            del_num = nums[r - k]
            in_num = nums[r]
            to_be_deleted[del_num] += 1
            if in_num <= -max_heap[0]:
                heapq.heappush(max_heap, -in_num)
                if del_num > -max_heap[0]:
                    self.rebalance(max_heap, min_heap)
            else:
                heapq.heappush(min_heap, in_num)
                if del_num <= -max_heap[0]:
                    self.rebalance(min_heap, max_heap)
            self.check_valid(to_be_deleted, max_heap, min_heap)
            ans.append(self.get_median(max_heap, min_heap, k))
        return ans

    def rebalance(self, from_heap, to_heap):
        heapq.heappush(to_heap, -heapq.heappop(from_heap))

    def check_valid(self, to_be_deleted, left, right):
        while to_be_deleted[-left[0]]:
            to_be_deleted[-left[0]] -= 1
            heapq.heappop(left)
        while right and to_be_deleted[right[0]]:
            to_be_deleted[right[0]] -= 1
            heapq.heappop(right)

    def get_median(self, left, right, k):
        if k & 1:
            return -left[0]
        return (-left[0] + right[0]) / 2
