'''
189. Rotate Array


Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


'''


#not my idea

class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nb = len(nums)
        k = k % nb
        self.reverse(nums, 0, nb - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, nb - 1)


# cpp, brute force

'''
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        for (int i = 0; i < k; ++i) shift1(nums);
        
    }
    
    void shift1(vector<int>& nums){
        int prev = nums.back();
        for (int i = 0; i < nums.size(); ++i){
            int curr = nums[i];
            nums[i] = prev;
            prev = curr;            
        }
    }
};
'''