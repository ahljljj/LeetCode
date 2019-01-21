/*
491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

*/

// cpp, wrong solution, unable to deal with duplicates

class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> res;
        queue<vector<int>> q;
        for (int i = 0; i < nums.size(); ++i){
            if (i == 0 || nums[i] != nums[i - 1]) q.push({i});
        }
        while (!q.empty()){
            vector<int> prev = q.front(); q.pop();
            int i = prev.back();
            for (int j = i + 1; j < nums.size(); ++j){
                if (nums[j] >= nums[i] && (j == i + 1 || nums[j] != nums[j - 1])){
                    vector<int> curr = prev; curr.push_back(j);
                    q.push(curr);
                    vector<int> tmp;
                    for (auto node : curr) tmp.push_back(nums[node]);
                    res.push_back(tmp);
                }
            }
        }
        return res;

    }
};