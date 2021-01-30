'''
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''


#44 / 44 test cases passed. Runtime: 32 ms 82.4%

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nb = len(nums)
        unums = set(nums)
        for num in unums:
            if nums.count(num) > nb // 2:
                return num


'''
# majority vote solution

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, cand = 0, 0
        for num in nums:
            if num == cand:
                cnt += 1
            elif cnt == 0:
                cand, cnt = num, 1
            else:
                cnt -= 1
        return cand if nums.count(cand) > len(nums)//2 else None

'''

#cpp, extra space, rewrite

'''
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> m;
        for (int &num: nums) ++m[num];
        for (auto itr = m.begin(); itr != m.end(); ++itr){
            if (itr->second > nums.size() / 2) return itr->first;
        }
        return 0;
    }
};
'''

# 2021/01/29, divide and conquer
# 分治法的返加回值是majority元素
# 如果左边的majority与右边的majority元素一致，那么该元素即为整个数组的majority
# 否则的话，这两个majority中的一个必然是整个数组的majority
# 利用for loop 来暴力判断

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.div_conq(nums, 0, len(nums) - 1)

    def div_conq(self, nums, start, end):
        if start == end:
            return nums[start]
        m = (start + end) // 2
        left = self.div_conq(nums, start, m)
        right = self.div_conq(nums, m + 1, end)
        if left == right:
            return left
        left_count = sum(1 for i in range(start, end + 1) if nums[i] == left)
        right_count = sum(1 for i in range(start, end + 1) if nums[i] == right)
        return left if left_count > right_count else right