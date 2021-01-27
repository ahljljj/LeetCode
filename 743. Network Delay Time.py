# 743. Network Delay Time


# Runtime: 460 ms, faster than 71.52% of Python3 online submissions for Network Delay Time.
# Memory Usage: 16.2 MB, less than 73.94% of Python3 online submissions for Network Delay Time.

# 2021/01/25, bfs
# 加权bfs，有点难度，以前做过类似的题目
# 通过权重来判断是否遍历某个结点

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = collections.deque([k])
        graph = self.get_graph(n, times)
        d = [float("inf")] * n
        d[k - 1] = 0
        while q:
            front = q.popleft()
            for u, w in graph[front]:
                if d[front - 1] + w < d[u - 1]:
                    d[u - 1] = d[front - 1] + w
                    q.append(u)
        return max(d) if max(d) < float("inf") else -1

    def get_graph(self, n, times):
        m = {i + 1: [] for i in range(n)}
        for a, b, c in times:
            m[a].append([b, c])
        return m
