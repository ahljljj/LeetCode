"""
254. Factor Combinations


Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


"""


# dfs, tle

'''

class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], n, 2)
        
        return res
    
    def dfs(self, res, tmp, n, idx):
        if n <= 1:
            if len(tmp) > 1:
                res.append(tmp[:])
            return
        for i in range(idx, n + 1):
            if n % i:
                continue
            tmp.append(i)
            self.dfs(res, tmp, n // i, i)
            tmp.pop()
        return
'''


# modified dfs

class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], n, 2)
        return res

    def dfs(self, res, tmp, n, idx):
        if len(tmp) > 0:
            tmp.append(n)
            res.append(tmp[:])
            tmp.pop()
        for i in range(idx, int(math.sqrt(n)) + 1):
            if n % i == 0:
                tmp.append(i)
                self.dfs(res, tmp, n // i, i)
                tmp.pop()
        return


# failed python buy AC on C++

'''

class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        vector<int> tmp = {};
        dfs(res, tmp, n, 2);
        return res;      
    }
    
    void dfs(vector<vector<int>> &res, vector<int> &tmp, int n, int idx){
        if (n <= 1){
            if (tmp.size() > 1) res.push_back(tmp) ;           
        }
        for (int i = idx; i <= n; i++){
            if (n % i) continue;
            tmp.push_back(i);
            dfs(res, tmp, n / i, i);
            tmp.pop_back();            
        }
        
        
        
    }
};
'''


# 2021/01/31

# Runtime: 64 ms, faster than 34.07% of Python3 online submissions for Factor Combinations.
# Memory Usage: 14.2 MB, less than 57.57% of Python3 online submissions for Factor Combinations.

# 全子集标准模板
# 先将所有的unique factor 找出来
# 再利用全子集的想法来从unique factor set 中找出合适的子集


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        factors = self.get_unique_factors(n)
        factors.sort()
        self.dfs(factors, n, 0, ans, [])
        return ans

    def get_unique_factors(self, n):
        i = 2
        ans = []
        while i < n and i * i <= n:
            if n % i == 0:
                ans.append(i)
                if n // i != i: ans.append(n // i)
            i += 1
        return ans

    def dfs(self, nums, n, start, ans, subset):
        if subset:
            if math.prod(subset) == n:
                ans.append(subset[:])
                return
            if math.prod(subset) > n:
                return
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, n, i, ans, subset)
            subset.pop()