#ifndef TWOSUM_H
#define TWOSUM_H
#include <vector>
using namespace std;
#include<unordered_map>

/*
 * 1. Two Sum
 * 
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


 */

class twoSum
{
public:
    twoSum();
    ~twoSum();
    vector<int> twosum1(vector<int>& nums, int target) {
        unordered_map <int, int> map;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            if (map.find(nums[i]) == map.end()) {
                map[nums[i]] = i;
            }
        }
        for (int i = 0; i < nums.size(); i++){
            if (map.find(target - nums[i]) != map.end()){
                if (i != map[target - nums[i]]){                    
                    res.push_back(i);
                    res.push_back(map[target - nums[i]]);
                    return res;                    
                }
                
            }
        }      
        return res;       
}

};

#endif // TWOSUM_H
