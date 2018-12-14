'''
281. Zigzag Iterator

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].



'''

# brute force

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.idx1, self.idx2 = -1, -1

    def next(self):
        """
        :rtype: int
        """
        if self.idx1 < len(self.v1) - 1 and self.idx2 < len(self.v2) - 1:
            if (self.idx1 + self.idx2) % 2 == 0:
                self.idx1 += 1
                return self.v1[self.idx1]
            else:
                self.idx2 += 1
                return self.v2[self.idx2]
        if self.idx1 < len(self.v1) - 1:
            self.idx1 += 1
            return self.v1[self.idx1]
        if self.idx2 < len(self.v2) - 1:
            self.idx2 += 1
            return self.v2[self.idx2]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx1 < len(self.v1) - 1 or self.idx2 < len(self.v2) - 1:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())





# c++, iterator

'''
class ZigzagIterator {
private:
    queue<pair<vector<int>::iterator, vector<int>::iterator> > Q;
    
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (v1.size() > 0) Q.push(make_pair(v1.begin(), v1.end()));
        if (v2.size() > 0) Q.push(make_pair(v2.begin(), v2.end()));
        
    }

    int next() {
        vector<int>::iterator it = Q.front().first;
        vector<int>::iterator endit = Q.front().second;
        Q.pop();
        if (it + 1 != endit) Q.push(make_pair(it + 1, endit));
        return *it;
        
    }

    bool hasNext() {
        
        return ! Q.empty();
        
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */

'''