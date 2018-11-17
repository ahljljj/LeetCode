"""
419. Battleships in a Board


Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?



"""

# brilliant idea
# Going over all cells, we can count only those that are the "first" cell of the battleship. First cell will be defined as the most top-left cell. We can check for first cells by only counting cells that do not have an 'X' to the left and do not have an 'X' above them.


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not len(board) or not len(board[0]):
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i  > 0 and board[i - 1][j] == 'X':
                        continue
                    if j  > 0 and board[i][j - 1] == 'X':
                        continue
                    count += 1
        return count


# standard dfs
# time complexity: hard to analyze O(n * ?) ? = 1
# space complexity: O(n), maintain a matrix to record every visited node


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not len(board) or not len(board[0]):
            return 0
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(n):
            for j in range(m):
                # the node is X and hasn't been visited, we only count as we see X the first time
                # we then start from X and walk vertically/horizontally to label every X be visited until we see a dot
                if board[i][j] == 'X' and not visited[i][j]:
                    count += 1
                    self.dfs(board, visited, i, j, n, m)
        return count

    def dfs(self, board, visited, i, j, n, m):
        if -1 < i < n and -1 < j < m and not visited[i][j] and board[i][j] == 'X':
            visited[i][j] = True
            for (x, y) in self.directions:
                self.dfs(board, visited, i + x, j + y, n, m)


# standard bfs
# time complexity: O(n)
# extra space complexity: O(n)

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not len(board) or not len(board[0]):
            return 0
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and not visited[i][j]:
                    count += 1
                    queue = set([(i, j)])
                    self.bfs(board, visited, queue, n, m)
        return count

    def bfs(self, board, visited, queue, n, m):
        while queue:
            tmp = set()
            for (i, j) in queue:
                visited[i][j] = True
                for (x, y) in self.directions:
                    ni, nj = i + x, j + y
                    if -1 < ni < n and -1 < nj < m and board[ni][nj] == 'X' and not visited[ni][nj]:
                        visited[ni][nj] = True
                        tmp.add((ni, nj))
            queue = tmp




# standard union find

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0
        self.parents = {}
        self.rank = {}
        n = len(board)
        m = len(board[0])
        self.directions = [(-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    self.parents[(i, j)] = (i, j)
                    self.rank[(i, j)] = 1
                    for (x, y) in self.directions:
                        ni, nj = i + x, j + y
                        if -1 < ni < n and -1 < nj < m and board[ni][nj] == 'X':
                            self.union((i, j), (ni, nj))
                            break
        res = set()

        for node in self.parents:
            res.add(self.parents[node])
        return len(res)

    def find(self, node):
        if node != self.parents[node]:
            p = self.parents[node]
            self.parents[node] = self.find(p)
        return self.parents[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if self.rank[p1] > self.rank[p2]:
            p1, p2 = p2, p1
        self.parents[p1] = p2
        self.rank[p2] += self.rank[p1]





# modified union find
# remove find method
# use a counter to maintain the number of parents


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0
        self.parents = {}
        self.rank = {}
        self.count = 0
        n = len(board)
        m = len(board[0])
        self.directions = [(-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    self.parents[(i, j)] = (i, j)
                    self.rank[(i, j)] = 1
                    self.count += 1  # update counter when create a new parent
                    for (x, y) in self.directions:
                        ni, nj = i + x, j + y
                        if -1 < ni < n and -1 < nj < m and board[ni][nj] == 'X':
                            self.union((i, j), (ni, nj))
                            self.count -= 1  # update counter when merge two nodes
                            break
        return self.count

    def union(self, node1, node2):
        p1, p2 = self.parents[node1], self.parents[node2]  # do not need find function in this case
        if self.rank[p1] > self.rank[p2]:
            p1, p2 = p2, p1
        self.parents[p1] = p2
        self.rank[p2] += self.rank[p1]

# more on union find

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0
        self.parents = {}
        self.rank = {}
        n = len(board)
        m = len(board[0])
        self.directions = [(-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    self.parents[(i, j)] = (i, j)
                    self.rank[(i, j)] = 1
                    for (x, y) in self.directions:
                        ni, nj = i + x, j + y
                        if -1 < ni < n and -1 < nj < m and board[ni][nj] == 'X':
                            self.union((i, j), (ni, nj))
                            break
        res = set()
        for node in self.parents:
            res.add(self.parents[node])
        return len(res)

    def union(self, node1, node2):
        p1, p2 = self.parents[node1], self.parents[node2]  # do not need find function in this case
        # do not need the comparison function since the old/visited node always has big rank
        self.parents[p1] = p2
        self.rank[p2] += self.rank[p1]




