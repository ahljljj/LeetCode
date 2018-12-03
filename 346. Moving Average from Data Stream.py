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