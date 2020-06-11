'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Accepted
494,468
Submissions
1,028,032

'''



# 2020/06/11, two pointers, too hard


'''
Runtime: 52 ms, faster than 72.70% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.6 MB, less than 28.08% of Python3 online submissions for Trapping Rain Water.
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            sea_level = min(height[l], height[r])
            if height[l] == sea_level:
                l += 1
                while l < r and height[l] < sea_level:
                    ans += sea_level - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and height[r] < sea_level:
                    ans += sea_level - height[r]
                    r -= 1
        return ans

