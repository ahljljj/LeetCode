"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                tmp = p.next.val
                while p.next and p.next.val == tmp:
                    p.next = p.next.next
            else:
                p = p.next
        return dummy.next
