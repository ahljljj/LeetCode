'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''

#165 / 165 test cases passed. Runtime: 52 ms
#This running time beats 96.59% of python 3 submissions. May 2018

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
        current=head
        while current and current.next:
            if current.val==current.next.val:
                while current.next and current.val==current.next.val:
                    current.next=current.next.next
            current=current.next
        return head