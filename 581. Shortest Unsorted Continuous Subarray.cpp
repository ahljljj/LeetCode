/*
581. Shortest Unsorted Continuous Subarray


Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

*/

// cpp, sort

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> dummy = nums;
        sort(nums.begin(), nums.end());
        int l = -1, r;
        for (int i = 0; i < nums.size(); ++i){
            if (nums[i] != dummy[i]){
                if (l < 0) l = i;
                else r = i;
            }
        }
        return l > -1? r - l + 1 : 0;

    }
};

// cpp, stack

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        stack<int> stack;
        int l = nums.size(), r = 0;
        for (int i = 0; i < nums.size(); ++i){
            while (! stack.empty() && nums[stack.top()] > nums[i]){
                l = min(l, stack.top());
                stack.pop();
            }
            stack.push(i);
        }
        if (l == nums.size()) return 0;
        while (!stack.empty()) stack.pop();
        for (int i = nums.size() - 1; i > -1; --i){
            while (!stack.empty() && nums[stack.top()] < nums[i]){
                r = max(r , stack.top());
                stack.pop();
            }
            stack.push(i);
        }
        return r - l + 1;

    }
};