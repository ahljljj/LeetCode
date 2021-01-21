# 826. Most Profit Assigning Work

# Runtime: 480 ms, faster than 17.34% of Python3 online submissions for Most Profit Assigning Work.
# Memory Usage: 17.2 MB, less than 31.89% of Python3 online submissions for Most Profit Assigning Work.

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [(p, d) for p, d in zip(profit, difficulty)]
        jobs.sort()
        worker = sorted(worker)
        ans = 0
        position = len(worker)
        for i in range(len(jobs) - 1, -1, -1):
            p, d = jobs[i][0], jobs[i][1]
            new_position = self.search(worker, d)
            if new_position != -1 and new_position < position:
                count = position - new_position
                ans += p * count
                position = new_position
            if position == 0: return ans
        return ans

    def search(self, worker, diff):
        l, r = 0, len(worker) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if worker[m] >= diff:
                r = m
            else:
                l = m
        if worker[l] >= diff:
            return l
        if worker[r] >= diff:
            return r
        return -1

# 2021/01/21, two pointer

# Runtime: 364 ms, faster than 48.92% of Python3 online submissions for Most Profit Assigning Work.
# Memory Usage: 17.1 MB, less than 54.18% of Python3 online submissions for Most Profit Assigning Work.

# moving window [0, r], best 指的是在这个window中最优的那份工作的profit。由于worker是按照skill排好序的，后面的worker肯定可以做这个工作。


def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    jobs = [(d, p) for d, p in zip(difficulty, profit)]
    jobs.sort();
    worker.sort()
    r, best = 0, 0
    ans = 0
    for skill in worker:
        while r < len(jobs) and skill >= jobs[r][0]:
            best = max(best, jobs[r][1])
            r += 1
        ans += best
    return ans

