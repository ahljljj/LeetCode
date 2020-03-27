'''
969. Pancake Sorting
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]

2020/03/27
Runtime: 48 ms, faster than 24.24% of Python3 online submissions for Pancake Sorting.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Pancake Sorting.
'''


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        nums = []
        # define pair: pair[1] the current position of num in the array
        for i, num in enumerate(A):
            nums.append([num, i])
        nums.sort()
        res = []
        for i in range(len(nums) - 1, -1, -1):
            #print(nums)
            curr = nums[i]
            if curr[1] == i: continue
            if curr[1] != 0:
                res.extend([curr[1] + 1, i + 1])
            elif i != 0:
                res.append(i + 1)
            for j in range(i + 1):
                if nums[j][1] <= curr[1]:
                    nums[j][1] = i - (curr[1] - nums[j][1])
                else:
                    nums[j][1] = i - nums[j][1]
        return res