"""
456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

"""

# better brute force: TLE on python
# time complexity O(n^2)

class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        valley = float('inf')
        for i in range(len(nums)):
            valley = min(valley, nums[i])
            for j in range(i + 1, len(nums)):
                if valley < nums[j] < nums[i]:
                    return True
        return False

# better brute force: AC on C++
# time complexity: O(n^2)

'''
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int valley = INT_MAX;
        for(int i = 0; i < nums.size(); i++){
            valley = min(valley, nums[i]);
            for(int j = i + 1; j < nums.size(); j++){
                if(valley < nums[j] && nums[j] < nums[i]){
                    return true;
                }
            }
            
        }
        return false;        
    }
};

'''