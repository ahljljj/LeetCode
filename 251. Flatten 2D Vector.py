"""
251. Flatten 2D Vector


Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,2,3,4,5,6].
Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.


"""

# python stack cheating

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d[::-1]
        self.stack = []

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        elif self.vec:
            self.stack = self.vec.pop()[::-1]
            while self.vec and not self.stack:
                self.stack = self.vec.pop()[::-1]
            return True if self.stack else False
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


# 2020/05/03, two pointers

'''
Runtime: 92 ms, faster than 26.85% of Python3 online submissions for Flatten 2D Vector.
Memory Usage: 19.5 MB, less than 12.50% of Python3 online submissions for Flatten 2D Vector.
'''


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.row = 0
        self.col = 0

    def to_next(self):
        while self.row < len(self.v) and self.col == len(self.v[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        self.to_next()
        res = self.v[self.row][self.col]
        self.col += 1
        return res

    def hasNext(self) -> bool:
        self.to_next()
        return self.row < len(self.v)