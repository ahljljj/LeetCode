"""
365. Water and Jug Problem


You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

"""

# pass the test, but not correct


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if z > x + y or x * y == 0:
            return False
        if x > y:
            x, y = y, x
        if z % self.commonfactor(x, y) == 0:
            return True
        else:
            return False

    def commonfactor(self, x, y):
        factx = set()
        res = 1
        for i in range(2, x + 1):
            if x % i == 0:
                factx.add(i)
        for num in factx:
            if y % num == 0:
                res *= num
        return res


# briefly modify, i think it should be correct

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if z > x + y or x * y == 0:
            return False
        if x > y:
            x, y = y, x
        if z % self.commonfactor(x, y) == 0:
            return True
        else:
            return False

    def commonfactor(self, x, y):
        factx = set()
        facty = set()

        while x > 1:
            for i in range(2, x + 1):
                if x % i == 0:
                    x /= i
                    factx.add(i)
                    break
        while y > 1:
            for i in range(2, y + 1):
                if y % i == 0:
                    y /= i
                    facty.add(i)
                    break
        res = 1
        for num in factx & facty:
            res *= num
        return res