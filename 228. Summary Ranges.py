"""
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


"""

#space complicity: O(n)
#time complicity: O(n)

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        tmp = []
        for num in nums:
            if not tmp:
                tmp.append([num])
                continue
            if num - tmp[-1][-1] == 1:
                tmp[-1].append(num)
            else:
                tmp.append([num])
        for row in range(len(tmp)):
            if len(tmp[row]) == 1:
                res.append(str(tmp[row][0]))
            else:
                res.append(str(tmp[row][0])+'->'+str(tmp[row][-1]))
        return res

'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        for num in nums:
            if not res:
                res.append([num])
                continue
            if num - res[-1][-1] == 1:
                res[-1][1:] = [num]
            else:
                res.append([num])
        return ['->'.join(map(str, r)) for r in res]

'''