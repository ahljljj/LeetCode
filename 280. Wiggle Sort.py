"""
280. Wiggle Sort


Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]


"""

# sort, brute force

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 1
        while i < len(nums) - 1:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2

# c++, sort, brute force

'''
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        if (nums.empty()) return;
        sort(nums.begin(), nums.end());
        for(int i = 1; i < nums.size() - 1; i += 2) swap(nums, i, i + 1);
    }
    void swap(vector<int>& nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};

'''

# c++, onepass, brilliant

'''
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        if (nums.empty()) return;
        bool less = true;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (less){
                if (nums[i] > nums[i + 1]) swap(nums, i, i + 1);   
            }else {
                if (nums[i] < nums[i + 1]) swap(nums, i, i + 1);
            }
            less = !less;
        }
        
    }
    
    void swap(vector<int> & nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};

'''
