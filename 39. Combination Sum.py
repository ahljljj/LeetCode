"""
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


"""

# not my idea


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(nums, tmp, target, idx):
            if target < 0:
                return
            if target == 0:
                res.append(tmp[:])
                return
            for i in range(idx, len(nums)):
                tmp.append(nums[i])
                helper(nums, tmp, target - nums[i], i)
                tmp.pop()

        helper(candidates, [], target, 0)
        return res


# cpp, rewrite, backtrack

'''
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, candidates, tmp, target);
        return res;
        
    }
    
    void dfs(vector<vector<int>>& res, vector<int> & cand, vector<int> tmp, int target){
        if (target == 0){
            res.push_back(tmp); 
            return;
        }
        for (int & n: cand){
            if (n > target || (!tmp.empty() && n < tmp.back())) continue;
            tmp.push_back(n);
            dfs(res, cand, tmp, target - n);
            tmp.pop_back();
        }
    }
};
'''

# cpp, slight modify

'''
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, candidates, tmp, target, 0);
        return res;
        
    }
    
    void dfs(vector<vector<int>>& res, vector<int> & cand, vector<int> tmp, int target, int idx){
        if (target == 0){
            res.push_back(tmp); 
            return;
        }
        for (int i = idx; i < cand.size(); ++i){
            if (cand[i] > target) continue;
            tmp.push_back(cand[i]);
            dfs(res, cand, tmp, target - cand[i], i);
            tmp.pop_back();
        }
    }
};
'''
