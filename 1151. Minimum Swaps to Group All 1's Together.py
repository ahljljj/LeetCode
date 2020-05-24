'''
1151. Minimum Swaps to Group All 1's Together

Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.



Example 1:

Input: [1,0,1,0,1]
Output: 1
Explanation:
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: [0,0,0,1,0]
Output: 0
Explanation:
Since there is only one 1 in the array, no swaps needed.
Example 3:

Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation:
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].


Note:

1 <= data.length <= 10^5
0 <= data[i] <= 1
Accepted
5,019
Submissions
8,520

'''


# 2020/05/24, sliding window

'''
Runtime: 916 ms, faster than 27.27% of Python3 online submissions for Minimum Swaps to Group All 1's Together.
Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Minimum Swaps to Group All 1's Together.
'''


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = sum(data)
        l, r = 0, 0
        res = float("inf")
        cnt_zero = 0
        for r in range(len(data)):
            if data[r] == 0:
                cnt_zero += 1
            while r - l + 1 > k:
                if data[l] == 0:
                    cnt_zero -= 1
                l += 1
            if r - l + 1 == k:
                res = min(res, cnt_zero)
        return res
