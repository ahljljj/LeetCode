'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


'''
Time limit exceed: 200 / 202 test cases passed.


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num=0
        len_nums=len(nums)
        num_non_pos=0
        for num in nums:
            if num<=0:
                num_non_pos+=1
        if num_non_pos==len_nums:
            return max(nums)
        max_num_temp=0
        temp=0
        for i in range(len_nums):
            if nums[i]>0:
                max_num_temp=nums[i]
                j=i+1
                while j<len_nums:
                    if nums[j]>=0:
                        max_num_temp+=nums[j]
                        j+=1
                    else:
                        temp=nums[j]
                        k=j+1
                        while k<len_nums:
                            temp+=nums[k]
                            if temp>0:
                                max_num_temp+=temp
                                break
                            k+=1
                        j=k+1
            if max_num_temp>max_num:
                max_num=max_num_temp
        return max_num
                     

'''


# 2020/05/07, dynamic programming


'''
Runtime: 72 ms, faster than 34.99% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-float("inf")] * len(nums)
        res = -float("inf")
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] if dp[i-1] < 0 else nums[i] + dp[i - 1]
            res = max(res, dp[i])
        return res