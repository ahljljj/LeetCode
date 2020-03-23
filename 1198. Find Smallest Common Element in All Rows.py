'''
1198. Find Smallest Common Element in All Rows

Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5


Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.

2020/03/22, binary search

Runtime: 524 ms, faster than 78.80% of Python3 online submissions for Find Smallest Common Element in All Rows.
Memory Usage: 38.3 MB, less than 100.00% of Python3 online submissions for Find Smallest Common Element in All Rows.


'''


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for i in range(len(mat[0])):
            for j in range(1, len(mat)):
                # search mat[0][i] within mat[j]
                idx = self.search(mat[j], mat[0][i])
                if idx == False:
                    break
            if idx:
                return mat[0][i]
        return -1

    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m
            else:
                l = m
        if nums[l] == target or nums[r] == target:
            return True
        return False