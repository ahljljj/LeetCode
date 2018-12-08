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