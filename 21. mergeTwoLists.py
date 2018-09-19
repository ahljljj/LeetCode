'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#208 / 208 test cases passed. Runtime: 48 ms
# This running time beats 97.38% of python3 submissions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current=new=ListNode(None)
        while l1 and l2 :
            if l1.val < l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        while l1:
            current.next=l1
            l1=l1.next
            current=current.next
        while l2:
            current.next=l2
            l2=l2.next
            current=current.next
        return new.next