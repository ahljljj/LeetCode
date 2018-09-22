"""
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None: return

        mid = self.findmid(head)
        tmp = mid.next
        mid.next = None
        secondhead = self.reverse(tmp)
        while head and secondhead:
            tmp1 = head.next
            tmp2 = secondhead.next
            head.next = secondhead
            if tmp1: secondhead.next = tmp1
            head = tmp1
            secondhead = tmp2

    def findmid(self, head):
        slow = fast = head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev

    def reverse(self, head):
        curr = head
        dummy = head
        prev = ListNode(None)
        prev.next = head
        while curr:
            tmp = curr.next
            curr.next = head
            prev.next = tmp
            head = curr
            curr = tmp
        dummy.next = None
        return head



