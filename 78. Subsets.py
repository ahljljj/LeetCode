"""

78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], nums, 0)
        res.append([])
        return res

    def helper(self, res, tmp, nums, start):
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            res.append(tmp[:])
            self.helper(res, tmp, nums, i + 1)
            tmp.pop()

# cpp, rewrite, backtracking

'''
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res = {{}};
        vector<int> tmp;
        dfs(res, tmp, nums, 0);
        return res;
        
    }
    
    void dfs(vector<vector<int>> & res, vector<int> tmp, vector<int>& nums, int idx){
        for (int i = idx; i < nums.size(); ++i){
            tmp.push_back(nums[i]);
            res.push_back(tmp);
            dfs(res, tmp, nums, i + 1);
            tmp.pop_back();
        }
    }
};
'''