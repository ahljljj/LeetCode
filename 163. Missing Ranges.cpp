/*
163. Missing Ranges

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


*/

// cpp, deal with overflow

class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        if (nums.empty()) return {getRange(lower, upper)};
        vector<string> res;
        if (nums[0] > lower) res.push_back(getRange(lower, nums[0] - 1));
        for (int i = 0; i < nums.size() - 1; ++i){
            if (nums[i] != nums[i + 1] && nums[i + 1] > nums[i] + 1) res.push_back(getRange(nums[i] + 1, nums[i + 1] - 1));

        }
        if (upper > nums.back()) res.push_back(getRange(nums.back() + 1, upper));
        return res;
    }

    string getRange(int s, int e){
        return s == e ? to_string(s) : to_string(s) + "->" + to_string(e);
    }
};