'''
215. Kth Largest Element in an Array


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.


'''


'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # QuickSelect idea: AC in 52 ms
        # ---------------------------
        # clear idea, but use too much memory
        pivot = nums[len(nums)//2]
        left  = [l for l in nums if l < pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r > pivot]

        if k <= len(right):
            return self.findKthLargest(right, k)
        elif (k - len(right)) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))        
            
'''

'''
> 类型：PriorityQueue + MinHeap
> Time Complexity O(NlogK) 因为每次heap插入时间是log(1), 插入k个就是logk
> Space Complexity O(N)
关于heap的使用口诀：

maxheap: 更换heap[0]中的最大值，放入条件为：放入比heap[0]小的值，heap初始为float('inf')
minheap: 更换heap[0]中的最小值，放入条件为：放入比heap[0]大的值，heap初始为-float('inf')
import heapq
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = [-float('inf')] * k
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return min_heap[0]



'''

# quicksort

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        return self.helper(nums, 0, len(nums) - 1, k)
        
   
    def helper(self, nums, low, high, k):
        left, right = low, high
        pivot = nums[(low + high)//2]
        i = left
        while i <= right:
            if nums[i] < pivot:
                self.swap(nums, i, right)
                right -= 1
            elif nums[i] > pivot:
                self.swap(nums, i, left)
                left += 1
                i += 1
            else:
                i += 1
        if k  <= left: # k - 1 < left
            return self.helper(nums, low, left - 1, k)
        elif k - 1 > right:
            return self.helper(nums, right + 1, high, k)
        else:
            return pivot
        
                
                
                
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
'''

# 2020/03/26, similar to above

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth larget = n - k th smallest
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        # find kth smallest element in nums, here k is representing the index, and it starts from 0
        # only consider the index [start : end]
        # the following if ... return is necessary
        if start == end:
            return nums[k]
        l, r = start, end
        p = nums[(l + r) // 2]
        i = l
        while i <= r:
            if nums[i] > p:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] < p:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1;
                i += 1
            else:
                i += 1
        if k <= l:
            return self.partition(nums, start, l, k)
        # i is larger than or equal to r
        if k >= i:
            return self.partition(nums, i, end, k)
        return p


# cpp, rewrite, priority queue

'''
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq(k, INT_MIN);
        for(int &num: nums){
            if (num > pq.top()){
                pq.pop();
                pq.push(num);
            }
            if (pq.size() > k) pq.pop();
        }
        return pq.top();
        
    }
};
'''


'''
2020/03/26, two pointer, jiuzhang template
2020/05/23, revise, totally forget

Runtime: 68 ms, faster than 55.50% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.7 MB, less than 60.00% of Python3 online submissions for Kth Largest Element in an Array.
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth larget = n - k th smallest
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        # find kth smallest element in nums, here k is representing the index, and it starts from 0
        # only consider the index [start : end]
        # the following if ... return is not necessary
        if start == end:
            return nums[k]
        l, r = start, end
        p = nums[(l + r) // 2]
        while l <= r:
            while l <= r and nums[l] < p:
                l += 1
            while l <= r and nums[r] > p:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1;
                r -= 1
        # right <= left by stoping condition
        if k <= r:
            return self.partition(nums, start, r, k)
        if k >= l:
            return self.partition(nums, l, end, k)
        return nums[k]