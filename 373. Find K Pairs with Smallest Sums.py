"""
373. Find K Pairs with Smallest Sums


You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

"""

# heap
# time complexity O(n^2lg(k)) space complexity O(k)


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = []
        row = len(nums1)
        col = len(nums2)
        count = 0
        heapq.heapify(heap)
        for i in range(row):
            for j in range(col):
                if i == j == 0:
                    heapq.heappush(heap, [-(nums1[i] + nums2[j]), nums1[i], nums2[j]])
                    count += 1
                    continue
                if count >= k:
                    if -(nums1[i] + nums2[j]) > heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, [-(nums1[i] + nums2[j]), nums1[i], nums2[j]])
                else:
                    heapq.heappush(heap, [-(nums1[i] + nums2[j]), nums1[i], nums2[j]])
                    count += 1
        res = []
        while heap:
            tmp = heapq.heappop(heap)
            res.append([tmp[1], tmp[2]])
        return res



# modified heap
#Given the matrix for [1,7,11] and [2,4,6], we can do BFS from the top-left position to expand candidates from only right cell and bottom cell. Since we treat it as a graph, we need to skip visited vertices as I used a dictionary visited.

# suppose the k-th element is (i , j), the next element would be (i + 1, j) or (i , j + 1)
#We create a priority queue using the sum as the priority. Note that python uses a min heap so the next item you pop off of the heap will be the coords with the smallest sum. We know that the smallest pair are the items at (0,0). We also know that the next smallest pair must be at either (1,0) or (0,1) since the inputs are sorted. Using induction you could prove that this holds for all any arbitrary coordinate, which is left to the reader. When we push these items onto the heap, in logarithmic time the heap will put the smallest sum at the beginning of the heap. Therefore, whenever we pop something off of the heap we are guaranteed that it is the next smallest item. We iterate until there are no more potential pairs or we have len(ret) == k.

# time complexity O(klg(n)) space complexity O(n)
# every time we push the two neighbors of the minimal value into the heap


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        row = len(nums1)
        col = len(nums2)
        heap = [[nums1[0] + nums2[0], 0, 0]]
        visited = {}
        res = []
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < row and (i + 1, j) not in visited:
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                visited[(i + 1, j)] = 1
            if j + 1 < col and (i, j + 1) not in visited:
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
                visited[(i, j + 1)] = 1
        return res



