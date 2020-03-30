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

# 2020/03/30 sort

'''
Runtime: 96 ms, faster than 73.67% of Python3 online submissions for Wiggle Sort.
Memory Usage: 14.8 MB, less than 6.67% of Python3 online submissions for Wiggle Sort.
'''

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums) % 2 == 0:
            self.even_sort(nums, 0, len(nums) - 1)
        else:
            m = len(nums) // 2
            nums[m], nums[-1] = nums[-1], nums[m]
            self.even_sort(nums, 0, 2 * m - 1)

    def even_sort(self, nums, l, r):
        l += 1;
        r -= 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 2;
            r -= 2
