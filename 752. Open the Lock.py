'''
752. Open the Lock


You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.

'''

'''
2020/04/05, BFS, extreme slow

Runtime: 7132 ms, faster than 5.03% of Python3 online submissions for Open the Lock.
Memory Usage: 14.8 MB, less than 12.50% of Python3 online submissions for Open the Lock.

'''


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = list(deadends)
        if "0000" in deadends: return -1
        q = collections.deque(['0000'])
        visited = set(q)
        level = 1
        dirs = [1, -1]
        while q:
            size = len(q)
            for _ in range(size):
                code = q.popleft()
                for i in range(4):
                    for d in dirs:
                        ch = str((int(code[i]) + d) % 10)
                        new_code = code[:i] + ch + code[i+1:]
                        if new_code == target: return level
                        if new_code not in deadends and new_code not in visited:
                            visited.add(new_code)
                            q.append(new_code)
            level += 1
        return -1


# simple modeification: faster

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = list(deadends)
        if "0000" in deadends: return -1
        q = collections.deque(['0000'])
        visited = set(q)
        level = 0
        dirs = [1, -1]
        while q:
            size = len(q)
            for _ in range(size):
                code = q.popleft()
                if code == target: return level
                if code in deadends: continue
                for i in range(4):
                    for d in dirs:
                        ch = str((int(code[i]) + d) % 10)
                        new_code = code[:i] + ch + code[i+1:]
                        if new_code not in visited:
                            visited.add(new_code)
                            q.append(new_code)
            level += 1
        return -1

    # modification

    class Solution:
        def openLock(self, deadends: List[str], target: str) -> int:
            deadends = list(deadends)
            q = collections.deque(['0000'])
            visited = set(['0000'])
            level = 0
            while q:
                size = len(q)
                for _ in range(size):
                    code = q.popleft()
                    if code == target: return level
                    if code in deadends: continue
                    for nei in self.neighbors(code):
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                level += 1
            return -1

        def neighbors(self, code):
            for i in range(4):
                x = int(code[i])
                for d in (-1, 1):
                    nx = (x + d) % 10
                    yield code[:i] + str(nx) + code[i + 1:]