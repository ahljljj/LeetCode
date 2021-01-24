# 881. Boats to Save People


# Runtime: 456 ms, faster than 43.61% of Python3 online submissions for Boats to Save People.
# Memory Usage: 21 MB, less than 46.76% of Python3 online submissions for Boats to Save People.

# 这题的技巧性太强
# 如果最重的那个人不能和最轻的人pair，最重的人就独自坐船
# 题目的关键是一条船最多只能坐两个人

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            ans += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        return ans

