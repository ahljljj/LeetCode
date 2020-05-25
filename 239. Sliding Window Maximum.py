'''
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
Accepted
253,834
Submissions
601,897

'''


# 2020/05/24, sliding window + monotonic queue

'''
Runtime: 336 ms, faster than 40.10% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 26.3 MB, less than 7.69% of Python3 online submissions for Sliding Window Maximum.
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l, r = 0, 0
        ans = []
        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            while r - l + 1 > k:
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
            if r - l + 1 == k:
                ans.append(q[0])
        return ans
