"""
75. Sort Colors


Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

# quicksort


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, n - 1
        idx = 0
        while idx <= right:
            if nums[idx] == 0:
                self.swap(nums, idx, left)
                idx += 1
                left += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                self.swap(nums, idx, right)
                right -= 1

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


# cpp, rewrite

'''
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int idx = 0;
        while (idx <= r){
            if (nums[idx] == 1) ++idx;
            else if (nums[idx] == 0){
                swap(nums, l++, idx++);
            } else{
                swap(nums, r--, idx);
            }
        }
        
    }
    
    void swap (vector<int>& nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};

'''

# 2021/01/19, partition twice

# Runtime: 36 ms, faster than 47.69% of Python3 online submissions for Sort Colors.
# Memory Usage: 14.2 MB, less than 47.38% of Python3 online submissions for Sort Colors.

# 注意：partition 的作用是将小于 target 的数放到左侧，大于 target 的数放到右侧。左右两侧都是未排序的。
# partition 两次，每一次将0 和 (1, 2) 分开， 第二次将1 和 2分开。


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.partition(nums, 1)
        self.partition(nums, 2)
        return

    def partition(self, nums, k):
        l, r = 0, len(nums) - 1
        while l <= r:
            while l <= r and nums[l] < k: l += 1
            while l <= r and nums[r] >= k: r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1;
                r -= 1
        return