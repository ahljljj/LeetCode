/*
594. Longest Harmonious Subsequence

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.



*/

// cpp, ordered map

class Solution {
public:
    int findLHS(vector<int>& nums) {
        if (nums.empty()) return 0;
        int res = 0;
        map<int, int> freq;
        for (int i = 0; i < nums.size(); ++i){
            ++freq[nums[i]];
        }
        for (auto it = freq.begin(); it != freq.end(); ){
            auto curr = it;
            ++it;
            if (it != freq.end() && abs(it->first - curr->first) == 1) res = max(res, curr->second + it->second);
        }
        return res;
    }
};