"""
259. 3Sum Smaller


Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?


"""


# two pointers, O(n^2)


class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] >= target - nums[i]:
                    right -= 1
                else:
                    res += right - left
                    left += 1
        return res

# c++, binary search O(n^2lgn)

'''
class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = 0, right;
        for(int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++){
                right = binarySearch(nums, target - nums[i] - nums[j], j + 1);
                res += right - j;                
            }
        }
        return res;   
    }
    int binarySearch(vector<int>& nums, int target, int left){
        int right = nums.size() - 1, mid;
        while (left <= right){
            mid = (left + right) >> 1;
            if (nums[mid] >= target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }        
        }
        return left - 1;    
    }
};


'''

# 2020/03/27, two pointers
'''Runtime: 120 ms, faster than 83.30% of Python3 online submissions for 3Sum Smaller.
Memory Usage: 13.8 MB, less than 25.00% of Python3 online submissions for 3Sum Smaller.'''


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        # assume nums[i] <= nums[j] <= nums[k]
        for k in range(len(nums) - 1, -1, -1):
            res += self.find_pairs(nums, k, target)
        return res

    def find_pairs(self, nums, k, target):
        l, r = 0, k - 1
        # find number of pairs such that nums[l] + nums[r] + nums[k] < target
        target -= nums[k]
        res = 0
        while l <= r:
            if nums[l] + nums[r] >= target:
                r -= 1
            else:
                res += r - l
                l += 1
        return res

