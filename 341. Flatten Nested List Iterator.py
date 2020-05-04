"""
341. Flatten Nested List Iterator


Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].


"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = []

        self.createlist(nestedList)
        self.n = len(self.res)
        self.pt = -1

    def next(self):
        """
        :rtype: int
        """
        self.pt += 1
        return self.res[self.pt]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pt + 1 < self.n:
            return True

    def createlist(self, nested):
        for item in nested:
            if item.getInteger() != None:
                self.res.append(item.getInteger())
            else:
                self.createlist(item.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



'''

another thought



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for item in nestedList[::-1]:
            self.stack.append(item)
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            peek = self.stack[-1]
            if peek.isInteger():
                return True
            else:
                self.stack.pop()
                for node in peek.getList()[::-1]:
                    self.stack.append(node)            
        return False
    
        
            
            
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
'''





# cpp, rewrite

'''

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
    stack<NestedInteger> stk;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for(auto it = nestedList.rbegin(); it != nestedList.rend(); ++it) stk.push(*it);
        
    }

    int next() {
        auto tp = stk.top();
        stk.pop();
        return tp.getInteger();
        
    }

    bool hasNext() {
        while (!stk.empty()){
            auto curr = stk.top();
            if (curr.isInteger()) return true;
            stk.pop();
            vector<NestedInteger> v = curr.getList();
            for (auto it = v.rbegin(); it != v.rend(); ++it) stk.push(*it);           
        }
        return false;        
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
'''

# 2020/05/04, initialize within the constructor, not good

'''
Runtime: 68 ms, faster than 68.18% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Flatten Nested List Iterator.
'''

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.make_list(nestedList, self.list)
        self.pos = 0

    def next(self) -> int:
        res = self.list[self.pos]
        self.pos += 1
        return res

    def hasNext(self) -> bool:
        return self.pos < len(self.list)

    def make_list(self, nested, res):
        for inner_list in nested:
            if inner_list.isInteger():
                res.append(inner_list.getInteger())
            else:
                self.make_list(inner_list.getList(), res)