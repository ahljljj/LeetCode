'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''

'''
1st solution

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex=rowIndex+1
        if rowIndex == 0:
            return []
        rlist = [[1]]
        for i in range(1, rowIndex):
            rlist.append([1])
            for j in range(1, i + 1 - 1):
                rlist[i].append(rlist[i - 1][j - 1] + rlist[i - 1][j])
            rlist[i].append(1)
        return rlist[rowIndex-1]
        
#34 / 34 test cases passed.  Runtime: 36 ms
#Your runtime beats 95.29% of python3 submissions. 08/07/018 

'''