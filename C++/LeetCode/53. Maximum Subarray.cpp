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

// divide and conquer
/*
 * 1) Divide the given array in two halves
2) Return the maximum of following three
….a) Maximum subarray sum in left half (Make a recursive call)
….b) Maximum subarray sum in right half (Make a recursive call)
….c) Maximum subarray sum such that the subarray crosses the midpoint

The lines 2.a and 2.b are simple recursive calls. 
 * How to find maximum subarray sum such that the subarray crosses the midpoint? 
 * We can easily find the crossing sum in linear time. 
 * The idea is simple, find the maximum sum starting from mid point and ending at some point on left of mid, 
 * then find the maximum sum starting from mid + 1 and ending with sum point on right of mid + 1. 
 * Finally, combine the two and return.
 * */



class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    
        
        return maxSub(nums, 0, nums.size() - 1);
        
    }
    
    int maxSub(vector<int>& nums, int left, int right){
        // return if there is only one element
        if (left == right){
            return nums[left];
        }
        
        // find the middle point
        int mid = (left + right)/2;
        
        /* Return maximum of following three possible cases 
      a) Maximum subarray sum in left half 
      b) Maximum subarray sum in right half 
      c) Maximum subarray sum such that the subarray crosses the midpoint */
        
        return max({maxSub(nums, left, mid), 
                    maxSub(nums, mid + 1, right),
                   maxCrossmid(nums, left, mid, right)});        
    }
    
    int maxCrossmid(vector<int> & nums, int left, int mid, int right){
        int left_sum = INT_MIN, right_sum = INT_MIN, sum{0};
        // scan element from left of mid
        for (int i = mid; i >= left; i--){
            sum += nums[i];
            left_sum = max(sum, left_sum);
        }
        sum = 0;
        // scan element from right of mid
        for (int i = mid + 1; i <= right; i++){
            sum += nums[i];
            right_sum = max(sum, right_sum);            
        }
        // return the summation
        return left_sum + right_sum;        
    }
    
    
    
};