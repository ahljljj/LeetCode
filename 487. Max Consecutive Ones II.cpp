/*
487. Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

*/

// cpp, sliding window, two pointers

/*
explain

The idea is to keep a window [l, h] that contains at most k zero

The following solution does not handle follow-up, because nums[l] will need to access previous input stream
Time: O(n) Space: O(1)

*/

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0, zeros = 0, k = 1;
        for (int l = 0, r = 0; r < nums.size(); ++r){
            if (nums[r] == 0) ++zeros;
            while (zeros > k){
                if (nums[l++] == 0) --zeros;
            }
            res = max(res, r - l + 1);
        }
        return res;

    }
};

// cpp, follow up

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0, k = 1;
        queue<int> q;
        for (int l = 0, r = 0; r < nums.size(); ++r){
            if (nums[r] == 0) q.push(r);
            while (q.size() > k){
                l = q.front() + 1; q.pop();
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};

// 2020/03/27, python rewrite

/*
Runtime: 452 ms, faster than 23.60% of Python3 online submissions for Max Consecutive Ones II.
Memory Usage: 14.2 MB, less than 12.50% of Python3 online submissions for Max Consecutive Ones II.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r, zeros = 0, 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 0: zeros += 1
            while zeros > 1 and l < r:
                if nums[l] == 0: zeros -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
*/