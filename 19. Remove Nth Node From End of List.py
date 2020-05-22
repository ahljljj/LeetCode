'''
19. Remove Nth Node From End of List


Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


'''



# not my idea



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        first = dummy
        second = dummy
        i=1
        while i < n+2:
            first = first.next
            i += 1
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


# 2020/05/22, two pointer

'''
Runtime: 60 ms, faster than 5.69% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.
'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        fast = slow = dummy
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        node = slow.next
        slow.next = node.next
        return dummy.next