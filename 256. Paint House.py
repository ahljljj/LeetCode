"""
256. Paint House


There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.



"""

# dynamic programming

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dpr, dpb, dpg = [0] * len(costs), [0] * len(costs), [0] * len(costs)
        res = float('inf')
        for i in range(len(costs)):
            if i == 0:
                dpr[i], dpb[i], dpg[i] = costs[0][0], costs[0][1], costs[0][2]
                res = min([dpr[i], dpb[i], dpg[i]])
                continue
            dpr[i] = costs[i][0] + min(dpb[i - 1], dpg[i - 1])
            dpb[i] = costs[i][1] + min(dpr[i - 1], dpg[i - 1])
            dpg[i] = costs[i][2] + min(dpb[i - 1], dpr[i - 1])
            res = min([dpr[i], dpb[i], dpg[i]])
        return res if res < float('inf') else 0

# c++, rewrite

'''
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        int * dpr = new int[costs.size()], * dpb = new int[costs.size()], * dpg = new int[costs.size()];
        int res = INT_MAX;
        for (int i = 0; i < costs.size(); i++){
            if (i == 0){
                dpr[i] = costs[i][0];
                dpb[i] = costs[i][1];
                dpg[i] = costs[i][2];
                res = min({dpr[i], dpb[i], dpg[i]});
                continue;                
            }
            dpr[i] = costs[i][0] + min(dpb[i - 1], dpg[i - 1]);
            dpb[i] = costs[i][1] + min(dpr[i - 1], dpg[i - 1]);
            dpg[i] = costs[i][2] + min(dpb[i - 1], dpr[i - 1]);
            res = min({dpr[i], dpb[i], dpg[i]});
            
            
        }        
        return res;
        
    }
};

'''