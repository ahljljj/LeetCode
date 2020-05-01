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

# bucket
#time complexity: O(n) space complexity: O(n)


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # save nums and the corresponding frequency to hashmap
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        # use buckets to  put the numer with same frequency into the same bucket
        buckets = {}
        for num, frequency in hashmap.items():
            if frequency not in buckets:
                buckets[frequency] = [num]
            else:
                buckets[frequency].append(num)
        # iterate over the buckets from the maximum possible maxfrequency unitl the accumulate frequency = k
        maxfrequency = 0
        res = []
        for i in range(len(nums), -1, -1):
            if i in buckets:
                maxfrequency += len(buckets[i])
                res.extend(buckets[i])
            if maxfrequency == k:
                return res


# cpp, rewrite

'''

class cmp
{
public:
    bool operator()(pair<int,int> &p1,pair<int,int> &p2) {
        return p1.second < p2.second;
    }
};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for (int &num: nums) ++m[num];
        auto cmp = [](pair<int,int> p1,pair<int,int> p2){return p1.second > p2.second;};
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        while (pq.size() < k) pq.push(make_pair(INT_MIN, INT_MIN));
        for (auto it = m.begin(); it != m.end(); ++it){
            auto tp = pq.top();
            if (it->second > tp.second) pq.push(make_pair(it->first, it->second));
            if (pq.size() > k) pq.pop();
        }
        vector<int> res;
        while(!pq.empty()) {
            auto curr = pq.top();
            res.push_back(curr.first);
            pq.pop();
        }
        return res;
        
    }
};
'''

# 2020/05/01, hashtable + min heap
'''
Runtime: 116 ms, faster than 22.98% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.2 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        heap = []
        for num, freq in m.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for freq, num in heap:
            res.append(num)
        return res
