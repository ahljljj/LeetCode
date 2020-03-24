"""
275. H-Index II

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?


"""


'''
Just binary search, each time check citations[mid]
case 1: citations[mid] == len-mid, then it means there are citations[mid] papers that have at least citations[mid] citations.
case 2: citations[mid] > len-mid, then it means there are citations[mid] papers that have moret than citations[mid] citations, so we should continue searching in the left half
case 3: citations[mid] < len-mid, we should continue searching in the right side

After iteration, it is guaranteed that right+1 is the one we need to find (i.e. len-(right+1) papars have at least len-(righ+1) citations)
'''



class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        return n - (right + 1)


'''
2020/03/23, binary search
idea: similar to copy books
Runtime: 184 ms, faster than 7.37% of Python3 online submissions for H-Index II.
Memory Usage: 19.6 MB, less than 50.00% of Python3 online submissions for H-Index II.
'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0: return 0
        l, r = 0, citations[-1]
        while l + 1 < r:
            m = (l + r) // 2
            if self.find_large(citations, m) <= m:
                r = m
            else:
                l = m
        if self.find_large(citations, r) >= r:
            return min(n, r)
        else:
            return min(n, l)

    def find_large(self, citations, target):
        res = 0
        for c in citations:
            if c >= target:
                res += 1
        return res