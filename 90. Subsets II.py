"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


"""


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        self.helper(res, [], nums, 0)
        res.append([])
        return res

    def helper(self, res, tmp, nums, idx):
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            if tmp not in res: res.append(tmp[:])
            self.helper(res, tmp, nums, i + 1)
            tmp.pop()

'''
2019/11/27, c++, backtracking, not that good

Runtime: 8 ms, faster than 83.30% of C++ online submissions for Subsets II.
Memory Usage: 10.1 MB, less than 31.82% of C++ online submissions for Subsets II.



class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        set<vector<int>> res;
        vector<int> tmp;
        backtracking(nums, res, tmp, 0);
        vector<vector<int>> target;
        for (auto &node: res) target.push_back(node);
        return target;
        
    }
    
    void backtracking(vector<int> &nums, set<vector<int>> &res, vector<int> tmp, int start){
        res.insert(tmp);
        for (int i = start; i < nums.size(); ++i){
            tmp.push_back(nums[i]);
            backtracking(nums, res, tmp, i + 1);
            tmp.pop_back();
        }
    }
};
'''


# 2020/04/14, backtracking + duplicates

'''
Runtime: 40 ms, faster than 39.29% of Python3 online submissions for Subsets II.
Memory Usage: 14.1 MB, less than 6.38% of Python3 online submissions for Subsets II.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, res, [], 0)
        return res

    def dfs(self, nums, res, subset, pos):
        if not nums: return
        res.append(subset[:])
        for i in range(pos, len(nums)):
            # only accept the first num if duplication happen
            if i > pos and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, res, subset, i + 1)
            subset.pop()