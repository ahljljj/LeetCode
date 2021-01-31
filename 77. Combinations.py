"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], n, k, 0)
        return res

    def helper(self, res, tmp, n, k, start):
        if k == 0:
            res.append(tmp[:])
            return
        for i in range(start, n):
            tmp.append(i + 1)
            self.helper(res, tmp, n, k - 1, i + 1)
            tmp.pop()


#cpp, backtracking, rewrite

'''
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, tmp, 1, n, k);
        return res;
        
    }
    
    void dfs(vector<vector<int>> &res, vector<int> tmp, int idx, int n, int k){
        if (tmp.size() == k){
            res.push_back(tmp); return;
        }
        for (int i = idx; i <= n; ++i){
            tmp.push_back(i);
            dfs(res, tmp, i + 1, n, k);
            tmp.pop_back();
        }
    }
};

'''


# 2021/01/31

# 全子集标准模板
# 只有当子集的长度 = k 时，才会append

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(n, k, 1, ans, [])
        return ans

    def dfs(self, n, k, start, ans, subset):
        if len(subset) == k:
            ans.append(subset[:])
            return
        for i in range(start, n + 1):
            subset.append(i)
            self.dfs(n, k, i + 1, ans, subset)
            subset.pop()