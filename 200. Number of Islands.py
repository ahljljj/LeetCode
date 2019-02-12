"""
200. Number of Islands


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        # number of islands
        count = 0
        self.dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.rows = len(grid)
        self.cols = len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    count += 1
                    self.helper(grid, i, j)
        return count

    def helper(self, grid, row, col):
        # edge/condition
        if row < 0 or row > self.rows - 1 or col < 0 or col > self.cols - 1 or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        for (i, j) in self.dirs:
            neiX = row + i
            neiY = col + j
            self.helper(grid, neiX, neiY)


# cpp, dfs, rewrite

'''
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int res = 0;
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (grid[i][j] == '1') {
                    ++res;
                    dfs(grid, visited, m, n, {i, j});
                }
            }
        }        
        return res;
        
    }
    
    void dfs(vector<vector<char>>& grid, vector<vector<bool>> &visited, int m, int n, vector<int> s){
        vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        int x = s[0], y = s[1];
        grid[x][y] = '0';
        for(auto &dir: dirs){
            int nx = s[0] + dir[0], ny = s[1] + dir[1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == '1')
                dfs(grid, visited, m, n, {nx, ny});
        }
        
    }
};
'''
