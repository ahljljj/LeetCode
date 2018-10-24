"""
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


"""


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