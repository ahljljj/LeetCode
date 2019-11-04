'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


'''

'''
brute force
time limit exceeded


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nb=len(nums)
        result=[]
        nums.sort()
        for i in range(nb):
            for j in range(i+1,nb):
                for k in range(j+1,nb):
                    if nums[i]+nums[j]+nums[k]==0:
                        if [nums[i],nums[j],nums[k]] not in result:
                            result.append([nums[i],nums[j],nums[k]])
                            break
        return result
        


'''


#two pointers, not my idea

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        nb = len(nums)
        for i in range(nb):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, nb - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp < 0:
                    l += 1
                elif tmp > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return result

'''
11-03-2019

Runtime: 96 ms, faster than 84.30% of C++ online submissions for 3Sum.
Memory Usage: 14.7 MB, less than 94.12% of C++ online submissions for 3Sum.

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); ++i){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1, r = nums.size() - 1;
            while (l < r){
                int s = nums[i] + nums[l] + nums[r];
                if (s < 0) ++l;
                else if (s > 0) --r;
                else{
                    res.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    while(l < r && nums[l] == nums[l + 1]) ++l;
                    while(l < r && nums[r] == nums[r - 1]) --r;
                    ++l; --r;
                }
            }
        }
        return res;
        
    }
};
'''