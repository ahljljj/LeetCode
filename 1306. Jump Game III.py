# 1306. Jump Game III

# 2021/01/27

# Runtime: 348 ms, faster than 5.04% of Python3 online submissions for Jump Game III.
# Memory Usage: 21 MB, less than 48.13% of Python3 online submissions for Jump Game III.


# standard bfs

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque([start])
        visited = [False] * len(arr)
        visited[start] = True
        while q:
            front = q.popleft()
            if arr[front] == 0: return True
            for i in [front + arr[front], front - arr[front]]:
                if i < 0 or i >= len(arr) or visited[i]:
                    continue
                q.append(i)
                visited[i] = True
        return False
