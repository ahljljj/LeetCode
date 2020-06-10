'''
295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
Accepted
182,258
Submissions
429,947

'''

# 2020/05/02, heap

'''
Runtime: 280 ms, faster than 29.50% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 25 MB, less than 6.67% of Python3 online submissions for Find Median from Data Stream.
'''


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        median = self.findMedian()
        if median == None or num < median:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                left_max = -heapq.heappop(self.left)
                heapq.heappush(self.right, left_max)
            return
        heapq.heappush(self.right, num)
        if len(self.right) > len(self.left):
            right_min = heapq.heappop(self.right)
            heapq.heappush(self.left, -right_min)

    def findMedian(self) -> float:
        if not self.left and not self.right:
            return None
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 2020/06/10, two heaps

'''
Runtime: 216 ms, faster than 55.68% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 24.9 MB, less than 61.66% of Python3 online submissions for Find Median from Data Stream.
'''


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # python default: min stack/ contain all num <= median
        # max stack: reverse of min stack/ contain all num > median
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        # min heap <= max heap <= min heap + 1
        self.balance()

    def balance(self):
        while len(self.min_heap) > len(self.max_heap):
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_val)
        while len(self.max_heap) > len(self.min_heap) + 1:
            max_val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_val)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]