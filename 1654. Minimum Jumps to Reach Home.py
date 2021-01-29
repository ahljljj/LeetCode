# 1654. Minimum Jumps to Reach Home

# 2021/01/28
# Runtime: 120 ms, faster than 49.35% of Python3 online submissions for Minimum Jumps to Reach Home.
# Memory Usage: 15 MB, less than 58.78% of Python3 online submissions for Minimum Jumps to Reach Home.

# 标准 bfs， 细节很多吧，不是很好写
# 最多只能退一次，最远点是 max (x, forbidden) + a + b

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = collections.deque([(0, 0)])
        step = 0
        furthest = max([x] + forbidden) + a + b
        forbidden = set(forbidden)
        visited = set()
        while q:
            size = len(q)
            for _ in range(size):
                front, direction = q.popleft()
                if front == x: return step
                if (front, direction) in visited: continue
                visited.add((front, direction))
                for move in [front + a, front - b]:
                    if move in forbidden: continue
                    if move > front:
                        if move <= furthest: q.append((move, 1))
                    elif direction != -1:
                        if move >= 0: q.append((move, -1))
            step += 1
        return -1