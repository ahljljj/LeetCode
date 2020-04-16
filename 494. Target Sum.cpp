/*
494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

*/

// cpp, dfs, extremely slow

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int res = 0, tmp = 0;
        dfs(nums, res, tmp, S, 0);
        return res;

    }

    void dfs(vector<int> & nums, int & count, int tmp, int target, int idx){
        if (idx == nums.size()) {
            if (tmp == target)++count;
            return;
        }
        dfs(nums, count, tmp + nums[idx], target, idx + 1);
        dfs(nums, count, tmp - nums[idx], target, idx + 1);
        return;
    }
};

// cpp, dynamic programming

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int dp[nums.size()][2001] = {};
        dp[0][nums[0] + 1000] = 1;
        dp[0][-nums[0] + 1000] += 1;
        for (int i = 1; i < nums.size(); ++i){
            for (int j = -1000; j <= 1000; ++j){
                if (dp[i - 1][j + 1000] > 0){
                    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000];
                    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000];
                }
            }
        }
        return S > 1000? 0 : dp[nums.size() - 1][S + 1000];

    }
};



/*
brute force DFS, time limit exceeded

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        self.dfs(nums, S, 0, 0)
        return self.res

    def dfs(self, nums, target, calculation, pos):
        if pos == len(nums):
            if calculation == target:
                self.res += 1
            return
        self.dfs(nums, target, calculation + nums[pos], pos + 1)
        self.dfs(nums, target, calculation - nums[pos], pos + 1)

# better DFS, still time limit exceeded

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        self.dfs(nums, S, 0, memo)
        return sum([x == S for x in memo[0]])

    def dfs(self, nums, target, pos, memo):
        if pos == len(nums):
            memo[pos] = [0]
            return memo[pos]
        calculations = []
        for num in self.dfs(nums, target, pos + 1, memo):
            calculations.append(nums[pos] + num)
            calculations.append(-nums[pos] + num)
        memo[pos] = calculations
        return memo[pos]

*/