'''
24. Swap Nodes in Pairs


Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.


'''



# be careful





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        curr = ListNode(0)
        dummy.next = head
        curr = head
        while curr and curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            prev.next = tmp
            curr = curr.next
            prev = tmp.next
        return dummy.next