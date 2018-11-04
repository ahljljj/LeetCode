"""

385. Mini Parser


Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.


"""



# wrong


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """


        if s[0] != "[":
            return NestedInteger(int(s))

        str_list = []
        tmp = ""
        for ch in s:
            if ch == "[":
                str_list.append(ch)
                if tmp: str_list.append(tmp)
            elif ch in ",]":
                if tmp: str_list.append(tmp)
                tmp = ""
                if ch == "]": str_list.append(ch)
            else:
                tmp += ch

        print("strlist", str_list)

        stack = []
        res = None
        for elem in str_list:
            if elem != "]":
                stack.append(elem)
            else:
                tmp = NestedInteger()
                while stack[-1] != "[":
                    curr = NestedInteger()
                    curr.add(int(stack.pop()))
                    for item in tmp.getList():
                        curr.add(item)
                    tmp = curr
                stack.pop()
                if res:
                    if res.getInteger():
                        tmp.add(res.getInteger())
                    else:
                        tmp.add(res.getList())
                res = tmp
        return res


# accepted / ridiculous slow

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        if s[0] != "[":
            return NestedInteger(int(s))

        str_list = []
        tmp = ""
        for ch in s:
            if ch == "[":
                str_list.append(ch)
                if tmp: str_list.append(tmp)
            elif ch in ",]":
                if tmp: str_list.append(tmp)
                tmp = ""
                if ch == "]": str_list.append(ch)
            else:
                tmp += ch

        stack = []
        for elem in str_list:
            if elem != "]":
                if elem == "[":
                    stack.append(elem)
                else:
                    stack.append(NestedInteger(int(elem)))
            else:
                res = NestedInteger()
                while stack[-1] != "[":
                    curr = NestedInteger()
                    top = stack.pop()
                    if top.getInteger() != None:
                        curr.add(top.getInteger())
                    else:
                        curr.add(top.getList())
                    for item in res.getList():
                        curr.add(item)
                    res = curr
                stack.pop()
                stack.append(res)

        return res


# reference / fast iteration, similar to the idea of recursion
# time complexity O(n)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        nums = ""
        stack = []
        last = None
        for ch in s:
            if ch == "[":
                elem = NestedInteger()
                if stack: stack[-1].add(elem)
                stack.append(elem) # append the physical address of this element to the end of the stack
            elif ch == ",":
                if nums:
                    stack[-1].add(NestedInteger(int(nums)))
                    nums = ""
            elif ch == "]":
                if nums:
                    stack[-1].add(NestedInteger(int(nums)))
                    nums = ""
                last = stack.pop()
            else:
                nums += ch
        return last if last else NestedInteger(int(nums))




# recursion hard to understand, just for record


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[':
            return NestedInteger(int(s))
        nested = NestedInteger()
        numP, start = 0, 1
        for i in range(1, len(s)):
            if (numP == 0 and s[i] == ',') or i == len(s) - 1:
                # make sure it is not an empty string
                if start < i:
                    nested.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == '[':
                numP += 1
            elif s[i] == ']':
                numP -= 1
        return nested




