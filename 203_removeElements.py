'''
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''

#not my idea

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        out = prev = ListNode(-1)
        prev.next = head
        current = head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return out.next
