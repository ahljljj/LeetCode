"""
213. House Robber II


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.


"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # rob_rf: rob this house
        # nrob_rf: not rob this house
        # rob_nrf: rob this house but not rob the first house
        # nrob_nrf: not rob this house and not rob the first house
        rob_rf, nrob_rf = nums[0], 0
        rob_nrf, nrob_nrf = 0, 0
        for num in nums[1:]:
            tmp = rob_rf
            rob_rf = num + nrob_rf
            nrob_rf = max(tmp, nrob_rf)

            tmp = rob_nrf
            rob_nrf = num + nrob_nrf
            nrob_nrf = max(tmp, nrob_nrf)

        return max(nrob_rf, rob_nrf, nrob_nrf)
