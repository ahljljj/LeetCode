"""
475. Heaters


Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses ca


"""

# cpp, rewrite

'''
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        vector<int> res (houses.size(), INT_MAX);
        for (int i = 0, h = 0; i < houses.size() && h < heaters.size();){
            if (houses[i] <= heaters[h]){
                res[i] = heaters[h] - houses[i];
                ++i;
                
            }            
            else
                ++h;            
        }
        for (int i = houses.size() - 1, h = heaters.size() - 1; i > -1 && h > -1;){
            if (houses[i] >= heaters[h]){
                res[i] = min(res[i], houses[i] - heaters[h]);
                --i;
            } else --h;
            
        }
        return *max_element(res.begin(), res.end());
        
    }
};

'''

# cpp, binary search

'''
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(heaters.begin(), heaters.end());
        int res = INT_MIN, curr;
        for (int i = 0; i < houses.size(); ++i){
            int idx = helper(heaters, houses[i]); // the least upper bound
//            cout << houses[i] << '\t' << idx << endl;
            if (idx > 0)
                curr = min(abs(heaters[idx] - houses[i]), abs(houses[i] - heaters[idx - 1]));
            else
                curr = abs(heaters[idx] - houses[i]);
            res = max(res, curr);            
        }
        return res;        
    }
    
    int helper(vector<int>& heaters, int target){
        
        if (target < heaters[0]) return 0;
        if (target > heaters[heaters.size() - 1]) return heaters.size() - 1;
        
        int res, left = 0, right = heaters.size() - 1, mid;
        while (left <= right){
            mid = (left + right) >> 1;
            if (heaters[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return left;
        
    }
};

'''