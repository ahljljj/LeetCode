"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
#not my idea

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                dfs(nums, tmp)
                tmp.pop()

        dfs(nums, [])
        return res


# python, backtracking

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, 0)
        return res

    def dfs(self, nums, res, idx):
        if idx == len(nums):
            res.append(nums[:])
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.dfs(nums, res, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]

# cpp, rewrite

'''
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        dfs(nums, res, 0);
        return res;
        
    }
    
    void swap(vector<int> & nums, int i , int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    void dfs(vector<int> &nums, vector<vector<int>> &res, int idx){
        if (idx == nums.size()) res.push_back(nums);
        for(int i = idx; i < nums.size(); ++i){
            swap(nums, i, idx);
            dfs(nums, res, idx + 1);
            swap(nums, i, idx);
        }
    }
};
'''


# 2020/04/19, DFS standard permutation

'''
Runtime: 64 ms, faster than 5.31% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Permutations.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, res, [], visited)
        return res

    def dfs(self, nums, result, permutation, visited):
        if len(permutation) == len(nums):
            result.append(permutation[:])
            return
        for i in range(len(nums)):
            if visited[i]: continue
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, result, permutation, visited)
            permutation.pop()
            visited[i] = False

