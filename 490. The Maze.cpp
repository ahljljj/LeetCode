/*
490. The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.



*/

// cpp, queue and bfs

class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int r = maze.size(), c = maze[0].size();
        vector<vector<bool>> visited(r, vector<bool>(c, false));
        queue<vector<int> > q; q.push(start); visited[start[0]][start[1]] = true;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while(!q.empty()){
            vector<int> curr = q.front(); q.pop();
//            visited[curr[0]][curr[1]] = true;
            if (curr == destination) return true;
            for (auto dir: dirs){
                int x = curr[0] + dir[0], y = curr[1] + dir[1];
                while ( x >= 0 && x < r && y >= 0 && y < c && maze[x][y] == 0){
                    x += dir[0]; y += dir[1];
                }
                if (!visited[x - dir[0]][y - dir[1]]){
                    q.push({x - dir[0], y - dir[1]});
                    visited[x - dir[0]][y - dir[1]] = true;
                }

            }
        }
        return false;
    }
};

// cpp, dfs AC

class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int r = maze.size(), c = maze[0].size();
        vector<vector<bool> > visited(r, vector<bool>(c, false));
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        return dfs(maze, visited, dirs, start, destination);


    }

    bool dfs(vector<vector<int>> & maze, vector<vector<bool>> & visited, int (&dirs)[4][2], vector<int> s, vector<int>& d){
        if (visited[s[0]][s[1]]) return false;
        if (s == d) return true;
        visited[s[0]][s[1]] = true;
        int r = maze.size(), c = maze[0].size();
        bool res = false;
        for (auto dir: dirs){
            int x = s[0] + dir[0], y = s[1] + dir[1];
            while ( x >= 0 && y >= 0 && x < r && y < c && maze[x][y] == 0){
                x += dir[0]; y += dir[1];
            }
            res = res || dfs(maze, visited, dirs, {x - dir[0], y - dir[1]}, d);
        }
        return res;
    }

};

// cpp, dfs AC, slight modification

class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int r = maze.size(), c = maze[0].size();
        vector<vector<bool> > visited(r, vector<bool>(c, false));
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        return dfs(maze, visited, dirs, start, destination);


    }

    bool dfs(vector<vector<int>> & maze, vector<vector<bool>> & visited, int (&dirs)[4][2], vector<int> s, vector<int>& d){
        if (visited[s[0]][s[1]]) return false;
        if (s == d) return true;
        visited[s[0]][s[1]] = true;
        int r = maze.size(), c = maze[0].size();
//        bool res = false;
        for (auto dir: dirs){
            int x = s[0] + dir[0], y = s[1] + dir[1];
            while ( x >= 0 && y >= 0 && x < r && y < c && maze[x][y] == 0){
                x += dir[0]; y += dir[1];
            }
            if (dfs(maze, visited, dirs, {x - dir[0], y - dir[1]}, d)) return true;
        }
        return false;
    }

};

/*
2020/04/04, python ugly codes

Runtime: 404 ms, faster than 22.16% of Python3 online submissions for The Maze.
Memory Usage: 14.3 MB, less than 15.38% of Python3 online submissions for The Maze.

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        q = collections.deque([start])
        visited = [[False] * m for _ in range(n)]
        while q:
            (x, y) = q.popleft()
            if [x, y] == destination: return True
            visited[x][y] = True
            ny = y
            while ny < m and maze[x][ny] != 1: ny += 1
            if not visited[x][ny - 1]:
                q.append([x, ny - 1])
                visited[x][ny - 1] = True
            ny = y
            while ny > -1 and maze[x][ny] != 1: ny -= 1
            if not visited[x][ny + 1]:
                q.append([x, ny + 1])
                visited[x][ny + 1] = True
            nx = x
            while nx < n and maze[nx][y] != 1: nx += 1
            if not visited[nx - 1][y]:
                q.append([nx - 1, y])
                visited[nx - 1][y] = True
            nx = x
            while nx > -1 and maze[nx][y] != 1: nx -= 1
            if not visited[nx + 1][y]:
                q.append([nx + 1, y])
                visited[nx + 1][y] = True
        return False


# better python code

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        q = collections.deque([start])
        visited = [[False] * m for _ in range(n)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            (x, y) = q.popleft()
            if [x, y] == destination: return True
            visited[x][y] = True
            for (deltaX, deltaY) in dirs:
                nx, ny = x + deltaX, y + deltaY
                # use while loop to find the stopping point
                while -1 < nx < n and -1 < ny < m and maze[nx][ny] != 1:
                    nx += deltaX; ny += deltaY
                # back track to the previous state
                # when the loop stops, only the following 3 cases happen:
                # nx = n, -1; ny = m, -1 or maze[nx][ny] = = -1
                nx -= deltaX; ny -= deltaY
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
        return False

*/