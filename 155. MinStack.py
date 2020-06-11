'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''


#
#18 / 18 test cases passed. runtime: 728 ms
#Your runtime beats 5.24% of python 3 submissions.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 2020/05/02, heap + stack, not good, O(lgN)

'''
Runtime: 80 ms, faster than 33.74% of Python3 online submissions for Min Stack.
Memory Usage: 17.6 MB, less than 5.36% of Python3 online submissions for Min Stack.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_heap = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.min_heap, x)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_heap[0]:
            heapq.heappop(self.min_heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]

# 2020/05/02, two stack, optimize O(1)

'''
Runtime: 104 ms, faster than 31.09% of Python3 online submissions for Min Stack.
Memory Usage: 17.4 MB, less than 5.36% of Python3 online submissions for Min Stack.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# 2020/06/11, two stack
'''
Runtime: 68 ms, faster than 49.40% of Python3 online submissions for Min Stack.
Memory Usage: 17.5 MB, less than 79.24% of Python3 online submissions for Min Stack.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.min_stack:
            self.min_stack.append(x)
        else:
            min_val = min(x, self.min_stack[-1])
            self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]