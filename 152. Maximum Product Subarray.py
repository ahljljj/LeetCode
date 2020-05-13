"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos , neg = nums[0], nums[0]
        maxprod = max(pos, neg)
        for num in nums[1:]:
            tmp1 , tmp2 = pos, neg
            pos = max(num, max(num * tmp1, num * tmp2))
            neg = min(num, min(num * tmp1, num * tmp2))
            maxprod = max(maxprod, max(pos, neg))
        return maxprod

# cpp, dynamic programming, rewrite

'''
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector<int> dpMin(nums.size()), dpMax(nums.size());
        dpMin[0] = dpMax[0] = nums[0];
        for (int i = 1; i < nums.size(); ++i){
            dpMax[i] = max(nums[i], max(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i]));
            dpMin[i] = min(nums[i], min(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i]));
        }
        return *max_element(dpMax.begin(), dpMax.end());
        
    }
};
'''


# 2020/05/13, two dp arrays

'''
Runtime: 60 ms, faster than 39.88% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 15 MB, less than 6.90% of Python3 online submissions for Maximum Product Subarray.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max, dp_min = [nums[0]], [nums[0]]
        for i in range(1, len(nums)):
            curr_max = max([nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1]])
            curr_min = min([nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1]])
            dp_max.append(curr_max)
            dp_min.append(curr_min)
        return max(dp_max)