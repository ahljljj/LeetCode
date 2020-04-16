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

// cpp, set AC

class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> resSet;
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
                    resSet.insert(tmp);
                }
            }
        }
        vector<vector<int>> res(resSet.begin(), resSet.end());

        return res;

    }
};

// cpp, backtracking

class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, tmp, nums, 0);
        return res;

    }

    void dfs(vector<vector<int>> & res, vector<int> &tmp, vector<int>& nums, int idx){
        if (tmp.size() > 1) res.push_back(tmp);
        unordered_set<int> s;
        for (int i = idx; i < nums.size(); ++i){
            if ((tmp.empty() || nums[i] >= tmp.back()) && s.find(nums[i]) == s.end()){
                tmp.push_back(nums[i]);
                dfs(res, tmp, nums, i + 1);
                tmp.pop_back();
                s.insert(nums[i]);
            }
        }
    }
};


/*
2020/04/16, subsets, unorder duplicates

Runtime: 224 ms, faster than 84.29% of Python3 online submissions for Increasing Subsequences.
Memory Usage: 21.4 MB, less than 50.00% of Python3 online submissions for Increasing Subsequences.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2: return []
        subsets = []
        self.dfs(nums, subsets, [], 0)
        return subsets

    def dfs(self, nums, subsets, subset, pos):
        if len(subset) > 1: subsets.append(subset[:])
        if pos == len(nums): return
        visited = set()
        for i in range(pos, len(nums)):
            if nums[i] in visited: continue
            if subset and nums[i] < subset[-1]: continue
            subset.append(nums[i])
            self.dfs(nums,subsets, subset, i + 1)
            subset.pop()
            visited.add(nums[i])


*/