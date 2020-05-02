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

# 2020/05/01, heap, AC, but not the right way to use heap
# time complexity O(Nlg(N)), not necessary to use heap

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


# 2020/05/02, heap O(Nlg(K))

'''
Runtime: 248 ms, faster than 16.72% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.4 MB, less than 18.18% of Python3 online submissions for Merge k Sorted Lists.
'''

ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = head = ListNode(None)
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)
        while heap:
            top = heapq.heappop(heap)
            head.next = top
            head = top
            if head.next:
                heapq.heappush(heap, head.next)
        return dummy.next

# 2020/05/02, bfs

'''
Runtime: 184 ms, faster than 25.83% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 12.12% of Python3 online submissions for Merge k Sorted Lists.
'''

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        q = collections.deque(lists)
        while len(q) > 1:
            l1 = q.popleft()
            l2 = q.popleft()
            q.append(self.merge2lists(l1, l2))
        return q[0]

    def merge2lists(self, l1, l2):
        dummy = head = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1: head.next = l1
        if l2: head.next = l2
        return dummy.next
