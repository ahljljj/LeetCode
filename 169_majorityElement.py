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