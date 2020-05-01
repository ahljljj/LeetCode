'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
Accepted
597,126
Submissions
1,530,982

'''

# 2020/05/01, heap

'''
Runtime: 112 ms, faster than 60.66% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.5 MB, less than 13.63% of Python3 online submissions for Merge k Sorted Lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        pos = 0
        for head in lists:
            while head:
                heapq.heappush(heap, (head.val, pos, head))
                head = head.next
                pos += 1
        if not heap: return None
        _, _, head = heapq.heappop(heap)
        curr = head
        while heap:
            curr.next = heap[0][2]
            _, _, curr = heapq.heappop(heap)
        return head

