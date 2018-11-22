"""
447. Number of Boomerangs


Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


"""

# hashtable, ridiculous slow
# space complexity O(n)
# time complexity O(n^2)


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            dist = {}
            p1 = points[i]
            for j in range(len(points)):
                p2 = points[j]
                tmp = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
                dist[tmp] = dist.get(tmp, 0) + 1
            for key in dist:
                length = dist[key]
                if length > 1:
                    res += length * (length - 1)
        return res


