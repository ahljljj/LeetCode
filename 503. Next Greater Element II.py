'''
503. Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

Accepted
90,389
Submissions
162,313


'''

# 2020/06/18, mono stack, loop twice

'''
Runtime: 248 ms, faster than 57.89% of Python3 online submissions for Next Greater Element II.
Memory Usage: 15.2 MB, less than 78.75% of Python3 online submissions for Next Greater Element II.
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # nums.append(-1)
        n = len(nums)
        ans = [-1] * n
        stack = []
        for r in range(2 * n):
            while stack and nums[stack[-1]] < nums[r % n]:
                top = stack.pop()
                ans[top] = nums[r % n]
            stack.append(r % n)
        return ans
