'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

#161 / 161 test cases passed. Runtime: 64 ms
# This running time beats 95.22% of python3 submissions. May 2018


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        j = 0
        num = nums[0]
        while i < n - 1:
            if nums[i] != nums[i + 1]:
                i += 1
                j += 1
                nums[j] = nums[i]
            else:
                i += 1
        return j + 1

'''
// cpp, rewrite

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 0, r = 0;
        while (r < nums.size()){
            while (r + 1 < nums.size() && nums[r] == nums[r + 1]) ++r;
            ++r;
            ++l;
            nums[l] = nums[r];
        }
        return l;
        
    }
};
'''

# 2020/03/26
'''
Runtime: 88 ms, faster than 55.47% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            if i < len(nums):
                target = nums[i]
                nums[count] = nums[i]
                count += 1; i += 1
                while i < len(nums) and nums[i] == target:
                    i += 1
        return count


