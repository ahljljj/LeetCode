"""
61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        first = second = ListNode(0)
        dummy = ListNode(0)
        first = second = dummy = head
        tmp = head
        i = 0
        while tmp:
            tmp = tmp.next
            i += 1

        if i <= 1: return head
        k = k % i

        if k == 0: return head

        i = 0

        while i <= k:
            first = first.next
            i += 1
        while first:
            first = first.next
            second = second.next
        new_head = ListNode(0)
        tmp = second.next
        second.next = None
        new_head.next = tmp
        while tmp.next:
            tmp = tmp.next
        tmp.next = dummy
        return new_head.next
