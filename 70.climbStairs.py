'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

''' recursion time limit exceed
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
        
'''

# just go from the other way (Fibonacci Number), the running time would be significantly improved. The following beats 100% of python 3 submissions.
#45 / 45 test cases passed. Runtime: 32 ms

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        climb1=1
        climb2=2
        for i in range(2,n):
            climb=climb1+climb2
            climb1=climb2
            climb2=climb
        return climb

# cpp, rewrite

'''
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = dp[1] = 1;
        for (int i = 2; i <= n; ++i) dp[i] = dp[i -1] + dp[i - 2];
        return dp[n];
        
    }
};
'''