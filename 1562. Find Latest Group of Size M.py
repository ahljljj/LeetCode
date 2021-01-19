# 1562. Find Latest Group of Size M

# 2021/01/19， union find ， too hard
# union find 变种题，看了评价区的答案
# 注意：1、每个结点size的初始值为0，代表当前结点的group为0；2、每次在union之前判断group size 是否等于 m，如果相等的话，对应的step是前一步的step。
# 3、最后一次join的那两个结点的group size是没办法验证的，所以做为edge case讨论。
# 这题感觉比较trick，感觉很验证说清楚

# Runtime: 2388 ms, faster than 9.95% of Python3 online submissions for Find Latest Group of Size M.
# Memory Usage: 41 MB, less than 10.90% of Python3 online submissions for Find Latest Group of Size M.

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return len(arr)
        uf = UnionFind(len(arr))
        ans = -1
        for step in range(len(arr)):
            node = arr[step] - 1
            uf.size[node] = 1
            for nei in (node - 1, node + 1):
                if 0 <= nei < len(arr) and uf.size[nei]:
                    if uf.size[uf.find(nei)] == m:
                        ans = step
                    uf.union(node, nei)
        return ans


class UnionFind:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.size = {i: 0 for i in range(n)}

    def find(self, node):
        root = node
        while root != self.parents[root]:
            root = self.parents[root]
        while node != root:
            old_root = self.parents[node]
            self.parents[node] = root
            node = old_root
        return root

    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA == rootB: return False
        if self.size[rootA] < self.size[rootB]:
            self.parents[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        else:
            self.parents[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        return True
