'''
531. Lonely Pixel I

Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
Accepted
20,495
Submissions
34,981

'''


# 2020/04/17, for loop

'''
Runtime: 508 ms, faster than 36.53% of Python3 online submissions for Lonely Pixel I.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Lonely Pixel I.
'''


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        res = 0
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B' and self.helper(picture, n, m, dirs, i, j):
                    res += 1
                    break
        return res

    def helper(self, matrix, n, m, dirs, i, j):
        for deltaI, deltaJ in dirs:
            x, y = i + deltaI, j + deltaJ
            while -1 < x < n and -1 < y < m and matrix[x][y] != 'B':
                x += deltaI;
                y += deltaJ
            if -1 < x < n and -1 < y < m:
                return False
        return True