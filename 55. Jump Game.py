"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.


"""

# not my idea

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_step = 0
        for i in range(len(nums)):
            if i > max_step: return False
            max_step = max(nums[i] + i, max_step)
        return True

# python, dp TLE

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1 if nums[0] > 0 else 0
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] > 0 and j + nums[j] >= i:
                    dp[i] = 1
        return dp[len(nums) - 1] > 0

# c++, rewrite

'''
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxStep = 0;
        for (int i = 0; i < nums.size(); ++i){
            if (maxStep < i) return false;
            maxStep = max(nums[i] + i, maxStep);
        }
        return true;
        
    }
};

'''

# c++, dp AC

'''
class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 1) return true;
        vector<int> dp(nums.size());
        if (nums[0] > 0) dp[0] = 1;
        for (int i = 1; i < nums.size(); ++i){
            for (int j = 0; j < i; ++j){
                if (dp[j] > 0 && nums[j] + j >= i) {
                    dp[i] = 1; break;
                }
            }
        }
        return dp.back() > 0;
        
    }
};
'''

# 2020/05/12, dp, tle

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None] * n
        dp[n-1] = True
        for i in range(n - 2, -1, -1):
            dp[i] = any([dp[1+i+j] for j in range(nums[i]) if 1 + i + j < n])
        return dp[0]


# 2020/05/12, greedy , too clever


'''
Runtime: 88 ms, faster than 77.98% of Python3 online submissions for Jump Game.
Memory Usage: 15.9 MB, less than 7.14% of Python3 online submissions for Jump Game.
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_good:
                last_good = i
        return last_good == 0


# 2020/05/12, dp or greedy? maximal jump capacity

'''

Runtime: 100 ms, faster than 29.31% of Python3 online submissions for Jump Game.
Memory Usage: 15.7 MB, less than 7.14% of Python3 online submissions for Jump Game.'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        reach = 0
        for i in range(len(nums)):
            if reach >= len(nums) - 1:
                return True
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
        return False