# 1129. Shortest Path with Alternating Colors

# 2021/01/27
# Runtime: 284 ms, faster than 5.18% of Python3 online submissions for Shortest Path with Alternating Colors.
# Memory Usage: 14.7 MB, less than 8.17% of Python3 online submissions for Shortest Path with Alternating Colors.

# 双重 bfs
# 从红图开始交替遍历路径 得到一条最短路
# 同样，从蓝图开始交替遍历得到另外一条最短路
# 二都取小值即可

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g_red = self.get_graph(n, red_edges)
        g_blue = self.get_graph(n, blue_edges)
        ans = []
        for i in range(n):
            d1 = self.search(g_red, g_blue, i, set(), set())
            d2 = self.search(g_blue, g_red, i, set(), set())
            if d1 != -1 and d2 != -1:
                ans.append(min(d1, d2))
            elif d1 != -1:
                ans.append(d1)
            else:
                ans.append(d2)
        return ans

    def search(self, g1, g2, dst, v1, v2):
        q = collections.deque([0])
        level = 0
        v1.add(0)
        while q:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                if front == dst: return level
                if level % 2 == 0:
                    for nei in g1[front]:
                        if nei not in v1:
                            q.append(nei)
                            v1.add(nei)
                else:
                    for nei in g2[front]:
                        if nei not in v2:
                            q.append(nei)
                            v2.add(nei)
            level += 1
        return -1

    def get_graph(self, n, edges):
        g = {i: [] for i in range(n)}
        for x, y in edges:
            g[x].append(y)
        return g