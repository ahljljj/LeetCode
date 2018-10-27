"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


# built-in function
#20 / 20 test cases passed. Runtime: 60 ms
#time complexity: O(nlgn)

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        tmp = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        res = []
        for (key, item) in tmp[:k]:
            res.append(key)

        return res


# hashmap + min heap: time complexity O(nlog(k)

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        min_heap = [[-float('inf'), -float("inf")]] * k
        heapq.heapify(min_heap)
        # min_heap: (value, key), sort by the first entry
        for key in hashmap:
            if hashmap[key] >= min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, [hashmap[key], key])
        res = []
        for node in min_heap:
            res.append(node[1])
        return res

