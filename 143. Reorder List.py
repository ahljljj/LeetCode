"""
143. Reorder List

<<<<<<< HEAD
=======

>>>>>>> 03447d33d86615a9944c8ef63e125326c791f5a9
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


"""

<<<<<<< HEAD
=======
'''
wrong
>>>>>>> 03447d33d86615a9944c8ef63e125326c791f5a9

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
<<<<<<< HEAD
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



=======
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
>>>>>>> 03447d33d86615a9944c8ef63e125326c791f5a9
