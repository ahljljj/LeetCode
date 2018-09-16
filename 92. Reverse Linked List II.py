"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL



"""


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head
        dummy = pre
        for i in range(1, m):
            pre = pre.next
        start = pre.next
        end = start
        for i in range(0, n - m):
            end = end.next
        for i in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = pre.next
            pre.next = tmp
            start = tmp
        return dummy.next

