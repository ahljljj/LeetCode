# 967. Numbers With Same Consecutive Differences


# 2021/01/27
# Runtime: 56 ms, faster than 20.10% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 15.1 MB, less than 10.05% of Python3 online submissions for Numbers With Same Consecutive Differences.
# 暴力bfs，细节很多，但是思路很简单
# 由低位向高位层序遍历。新的digit可以是新的最高位也可以是新的最低位
# 用visited数组来判断新产生的数已经遍历过

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = collections.deque([str(i) for i in range(10)])
        length = 1
        visited = set(q)
        while length < n:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                first, last = front[0], front[-1]
                prefix = [int(first) - k, int(first) + k]
                suffix = [int(last) - k, int(last) + k]
                for num in prefix:
                    if 0 <= num < 10 and str(num) + front not in visited:
                        q.append(str(num) + front)
                        visited.add(str(num) + front)
                for num in suffix:
                    if 0 <= num < 10 and front + str(num) not in visited:
                        q.append(front + str(num))
                        visited.add(front + str(num))
            length += 1
        ans = [int(num) for num in q if num[0] != '0']
        return ans

# 2021/01/27
# 经过优化后的bfs
# 由低位向高位层序遍历，每次新产生的数都是最低位


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = collections.deque( [str(i) for i in range(10)])
        length = 1
        visited = set(q)
        while length < n:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                suffix = [ int(front[-1]) - k ,   int(front[-1]) + k ]
                for num in suffix:
                    if 0 <= num < 10 and front + str(num) not in visited:
                        q.append( front + str(num) )
                        visited.add( front + str(num) )
            length += 1
        ans = [ int(num) for num in q if num[0] != '0' ]
        return ans

# 2021/01/27
# 进一步优化

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = collections.deque(range(1, 10))
        length = 1
        visited = set(q)
        while length < n:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                last = front % 10
                suffix = [ last - k , last + k ]
                for num in suffix:
                    if 0 <= num < 10 and front * 10 + num not in visited:
                        q.append( front * 10 + num )
                        visited.add( front * 10 + num )
            length += 1
        return list(q)

# 最终版
# Runtime: 32 ms, faster than 96.81% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 14.6 MB, less than 65.69% of Python3 online submissions for Numbers With Same Consecutive Differences.
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = collections.deque(range(1, 10))
        length = 1
        while length < n:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                last = front % 10
                suffix = [ last - k , last + k ] if k else [last]
                for num in suffix:
                    if 0 <= num < 10: q.append( front * 10 + num )
            length += 1
        return list(q)

