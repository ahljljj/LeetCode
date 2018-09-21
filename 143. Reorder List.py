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

'''
wrong

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: 
        void Do not return anything, modify head in-place instead.
        """
        self.helper(head)
        
    def pretail(self, head):
        tmp = head
        while tmp and tmp.next and tmp.next.next :
            print('while loop', tmp.val)
            tmp = tmp.next
        return tmp
    def helper(self, head):
        if head == None or head.next == None: return
        pretail = self.pretail(head)
        tmp = head.next
        tail = pretail.next
        head.next = tail
        pretail.next = None
        tail.next = self.helper(tmp)
        
        
        

'''