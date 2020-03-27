/*
485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
*/

// cpp version

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0, currMax = 0;
        for (int i = 0; i < nums.size(); ++i){
            if (nums[i] == 1)
            {
            ++currMax;
            res = max(res, currMax);
            }
            else
                currMax = 0;
        }

        return res;

    }
};


// 2020/03/27， python sliding window

/*

Runtime: 444 ms, faster than 5.80% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.2 MB, less than 7.69% of Python3 online submissions for Max Consecutive Ones.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r, zeros = 0, 0, 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0: zeros += 1
            while l <= r and zeros > 0:
                if nums[l] == 0: zeros -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
*/