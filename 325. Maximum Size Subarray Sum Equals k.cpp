/*
325. Maximum Size Subarray Sum Equals k

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?

*/

// cpp, hashtable

/*

The HashMap stores the sum of all elements before index i as key, and i as value. For each i, check not only the current sum but also (currentSum - previousSum) to see if there is any that equals k, and update max length.

PS: An "else" is added. Thanks to beckychiu1988 for comment.
*/

class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        int sum = 0, maxIdx = 0;
        for (int i = 0; i < nums.size(); ++i){
            sum += nums[i];
            if (sum == k) maxIdx = i + 1;
            else if (m.find(sum - k) != m.end()) maxIdx = max(maxIdx, i - m[sum - k]);
            if (m.find(sum) == m.end()) m[sum] = i;
        }
        return maxIdx;

    }
};