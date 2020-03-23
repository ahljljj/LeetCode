'''
1182. Shortest Distance to Target Color

You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.



Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation:
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.


Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3

2020/03/23, binary search

Runtime: 2288 ms, faster than 33.05% of Python3 online submissions for Shortest Distance to Target Color.
Memory Usage: 35.7 MB, less than 100.00% of Python3 online submissions for Shortest Distance to Target Color.

Basic idea is to group all indexes by color.
And for each index in the queries, do binary search on the color group.
'''


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_map = {}
        for i, color in enumerate(colors):
            if color not in color_map:
                color_map[color] = [i]
            color_map[color].append(i)
        res = []
        for q in queries:
            # c1, c2 = colors[q[0]], q[1]
            if q[1] not in color_map:
                res.append(-1)
            else:
                # search nearest distance to q[0] in color_map[q1]
                d = self.search(color_map[q[1]], q[0])
                res.append(d)
        return res

    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] == target:
                return 0
            elif nums[m] > target:
                r = m
            else:
                l = m
        if abs(nums[r] - target) < abs(target - nums[l]):
            return abs(nums[r] - target)
        else:
            return abs(target - nums[l])