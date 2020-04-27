"""
346. Moving Average from Data Stream


Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3


"""

# deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0
        self.front = collections.deque()
        self.size = size
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        if self.count < self.size:
            self.front.append(val)
            self.count += 1
            return self.sum / self.count
        self.sum -= self.front.popleft()
        self.front.append(val)
        return self.sum / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# 2020/04/27， deque

'''
Runtime: 64 ms, faster than 81.27% of Python3 online submissions for Moving Average from Data Stream.
Memory Usage: 17 MB, less than 9.52% of Python3 online submissions for Moving Average from Data Stream.
'''

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.stream = collections.deque([])
        self.res = 0

    def next(self, val: int) -> float:
        old_size = len(self.stream)
        self.stream.append(val)
        if len(self.stream) <= self.size:
            self.res = (self.res * old_size + val) / (old_size + 1)
        else:
            front = self.stream.popleft()
            self.res = (self.res * self.size - front + val) / self.size
        return self.res

# 2020/04/27, deque

'''
Runtime: 68 ms, faster than 65.97% of Python3 online submissions for Moving Average from Data Stream.
Memory Usage: 16.8 MB, less than 9.52% of Python3 online submissions for Moving Average from Data Stream.
'''

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.stream = collections.deque([])
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.stream) == self.size:
            self.sum -= self.stream.popleft()
        self.sum += val
        self.stream.append(val)
        return self.sum / len(self.stream)