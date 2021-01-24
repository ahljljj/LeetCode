# 986. Interval List Intersections


# Runtime: 152 ms, faster than 50.88% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.8 MB, less than 97.93% of Python3 online submissions for Interval List Intersections.

# 2021/01/24, two pointer
# 两个数组的two pointer，细节很多，但思想比较简单
# [a, b] 和 [c, d] 的交集是 [max(a, b), min(c, d)]，余下的就是判断怎么去update指标i和j
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][0]:
                i += 1
            else:
                left = max(firstList[i][0], secondList[j][0])
                right = min(firstList[i][1], secondList[j][1])
                ans.append([left, right])
                if firstList[i][1] > secondList[j][1]:
                    j += 1
                elif firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    i += 1;
                    j += 1
        return ans
