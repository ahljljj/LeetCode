'''
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000


'''


'''
2020/03/20, sort

Runtime: 660 ms, faster than 93.35% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.

'''


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0] ** 2 + x[1] ** 2)
        res = []
        for i in range(K):
            res.append(points[i])
        return res


# 2020/04/30, heap

'''
Runtime: 728 ms, faster than 53.69% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.8 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.
'''


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-x*x - y*y, x, y))
            if len(heap) > K:
                heapq.heappop(heap)
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res