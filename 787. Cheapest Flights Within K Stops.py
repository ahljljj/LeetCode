# 787. Cheapest Flights Within K Stops

# Runtime: 556 ms, faster than 7.15% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 15.8 MB, less than 55.43% of Python3 online submissions for Cheapest Flights Within K Stops.


# 2021/01/26, bfs, weighted graph, limit stop

# 加权bfs, 对层数有限制
# 核心是对最短路径以及层数进行记录

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = self.get_graph(n, flights)
        price = {(city, stop): float("inf") for city in range(n) for stop in range(K + 1)}
        price[(src, 0)] = 0
        q = collections.deque([(src, 0)])
        stop = 0
        while q and stop <= K:
            size = len(q)
            for _ in range(size):
                curr_node, curr_stop = q.popleft()
                for v, w in graph[curr_node]:
                    if price[(v, stop)] > price[(curr_node, curr_stop)] + w:
                        price[(v, stop)] = price[(curr_node, curr_stop)] + w
                        q.append((v, stop))
            stop += 1
        ans = min([price[(city, stop)] for city, stop in price if city == dst])
        return ans if ans < float("inf") else -1

    def get_graph(self, n, flights):
        m = {i: [] for i in range(n)}
        for u, v, w in flights:
            m[u].append([v, w])
        return m


