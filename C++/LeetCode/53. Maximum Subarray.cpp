/* 
 * 53. Maximum Subarray
 * 
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 * */
 
 // dynamic programming 8ms
 // time complexity O(n) space complexity O(n)
 
 
 class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        for (int i = 1; i < nums.size(); i++){
            if (dp[i - 1] <= 0){
                dp[i] = nums[i];
            }else{
                dp[i] = dp[i - 1] + nums[i];
            }
        }
        return *max_element(dp.begin(), dp.end());   
    } 
};

// slight change 8 ms


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        int res = dp[0];
        for (int i = 1; i < nums.size(); i++){
            if (dp[i - 1] <= 0){
                dp[i] = nums[i];
            }else{
                dp[i] = dp[i - 1] + nums[i];
            }
            res = max(res, dp[i]);
        }
        return res;   
    } 
};


// dynamic programming, slight change 4ms
// time complexity O(n) space complexity O(1)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int dp = nums[0];
        int res = dp;
        for (int i = 1; i < nums.size(); i++){
            if (dp <= 0){
                dp = nums[i];
            }else{
                dp += nums[i];
            }
            res = max(res, dp);
        }
        return res;   
    } 
};