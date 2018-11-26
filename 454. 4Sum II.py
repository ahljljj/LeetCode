"""
454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


"""

# hashmap
# time complexity O(n^2)
'''
ake the arrays A and B, and compute all the possible sums of two elements. Put the sum in the Hash map, and increase the hash map value if more than 1 pair sums to the same value.

Compute all the possible sums of the arrays C and D. If the hash map contains the opposite value of the current sum, increase the count of four elements sum to 0 by the counter in the map.

'''

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sumAB = {}
        for nA in A:
            for nB in B:
                tmp = nA + nB
                if tmp not in sumAB:
                    sumAB[tmp] = 1
                else:
                    sumAB[tmp] += 1
        sumCD = {}
        res = 0
        for nC in C:
            for nD in D:
                tmp = nC + nD
                if -tmp in sumAB:
                    res += sumAB[-tmp]
        return res

# binary search: TLE

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sumCD = []
        for nC in C:
            for nD in D:
                sumCD.append(nC + nD)
        sumCD.sort()
        res = 0
        for nA in A:
            for nB in B:
                target = -(nA + nB)
                right = self.upper(sumCD, target)
                if sumCD[right] != target:
                    continue
                left = self.lower(sumCD, target)
                res += right - left + 1
        return res


def upper(self, nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


def lower(self, nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1

# binary search: TLE

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sumCD = []
        for nC in C:
            for nD in D:
                sumCD.append(nC + nD)
        sumCD.sort()
        res = 0
        for nA in A:
            for nB in B:
                target = -(nA + nB)
                exist = self.biSearch(sumCD, target)
                if exist == -1:
                    continue
                right = self.upper(sumCD, exist, target)
                left = self.lower(sumCD, exist, target)
                res += right - left + 1
        return res

    def biSearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def upper(self, nums, lower, target):
        left, right = lower, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

    def lower(self, nums, upper, target):
        left, right = 0, upper
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right + 1


# barely accepted binary search
# time complexity O(n^2lgn)

'''
first add x (foreach in vector A) and y (foreach in vector B) ,put the sum into vector s,do the same to vector C,D and new vector called m; for every x in new vector s, we find how many -x in vector m, use binary search to do this ,This is the binary search code

'''

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sumCD = []
        sumAB = []
        for nC in C:
            for nD in D:
                sumCD.append(nC + nD)
        for nA in A:
            for nB in B:
                sumAB.append(nA + nB)
        sumCD.sort()
        sumAB.sort()
        res, tmp = 0, 0
        for i in range(len(sumAB)):
            target = - sumAB[i]
            if i > 0 and sumAB[i] == sumAB[i - 1]:
                res += tmp
            else:
                right = self.upper(sumCD, target)
                if sumCD[right] != target:
                    tmp = 0
                    continue
                left = self.lower(sumCD, target)
                tmp = right - left + 1
                res += tmp
        return res


    def upper(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right


    def lower(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left




