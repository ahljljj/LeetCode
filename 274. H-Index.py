"""
274. H-Index


Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.



"""

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        n = len(citations)
        h = {}
        for i in range(n):
            # count the number papers with citation <= i
            if citations[i] not in h:
                # if the paper was not used, compute the accumulated number of citations
                if i == 0:
                    h[citations[i]] = 1
                else:
                    h[citations[i]] = 1 + h[citations[i - 1]]
            else:
                h[citations[i]] += 1
        hidx = None
        for i in range(n - 1, -1, -1):
            # number of papers with citation >= citations[i] or > citations[i - 1]
            tmp = min(n - h[citations[i - 1]] if i > 0 else n, citations[i])
            if not hidx:
                hidx = tmp
                continue
            if tmp < hidx:
                return hidx
            else:
                hidx = tmp
        return hidx