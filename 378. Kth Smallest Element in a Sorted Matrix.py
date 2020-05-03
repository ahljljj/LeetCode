"""
378. Kth Smallest Element in a Sorted Matrix


Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.



"""

# heap: time complexity O(klgk) space complexity O(k)


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [[matrix[0][0], 0, 0]]
        n = len(matrix)
        m = len(matrix[0])
        heapq.heapify(heap)
        count = 0
        visited = set()
        while count < k:
            val, i, j = heapq.heappop(heap)
            count += 1
            if j + 1 < m:
                if (i, j + 1) not in visited:
                    heapq.heappush(heap, [matrix[i][j + 1], i, j + 1])
                    visited.add((i, j + 1))
            if i + 1 < n:
                if (i + 1, j) not in visited:
                    heapq.heappush(heap, [matrix[i + 1][j], i + 1, j])
                    visited.add((i + 1, j))
        return val


# binary search
# time complexity O(nlgn) it seems this runs faster than heap!!


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left, right = matrix[0][0], matrix[-1][-1]
        n = len(matrix)
        m = len(matrix[0])
        while left < right:
            mid = (left + right) >> 1
            count, j = 0, m - 1
            for i in range(n):
                while j > -1 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            if count < k:
                left = mid + 1
            else:
                right = mid  # important can not be mid - 1
        return left


# 2020/05/02, heap, o(klogn)

'''
Runtime: 224 ms, faster than 49.12% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.8 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i, row in enumerate(matrix):
            heapq.heappush(heap, (row[0], i, 0))
        order = 0
        while order < k:
            num, i, pos = heapq.heappop(heap)
            pos += 1
            if pos < len(matrix[i]):
                heapq.heappush(heap, (matrix[i][pos], i, pos))
            order += 1
        return num
