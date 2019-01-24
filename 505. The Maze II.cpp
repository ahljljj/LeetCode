/*
505. The Maze II

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

*/

// cpp, bfs, wrong solution

class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size(), n = maze[0].size();
        queue<vector<int>> q; vector<vector<bool>> visited(m, vector<bool>(n, false));
        q.push({start[0], start[1], 0}); visited[start[0]][start[1]] = true;
        int res = INT_MAX;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
//        bool find = false;
        while (!q.empty()){
            vector<int> curr = q.front();
            q.pop();
            if (vector<int>{curr[0], curr[1]} == destination){
//                cout << curr[0] << " " << curr[1] << " " << curr[2] << endl;
                res = min(res, curr[2]);
//                continue;
            }
            for (auto dir: dirs){
                int i = curr[0] + dir[0], j = curr[1] + dir[1], d = 0;
                while (i >= 0 && i < m && j >= 0 && j < n && maze[i][j] == 0){
                    i += dir[0]; j += dir[1]; ++d;
                }
                if (!visited[i - dir[0]][j - dir[1]]){
                    q.push({i - dir[0], j - dir[1], d + curr[2]}); visited[i - dir[0]][j - dir[1]] = true;
                }
            }
        }
        return res < INT_MAX ?res : -1;
    }
};