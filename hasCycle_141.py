'''

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# using set, not my idea


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        J=set()
        current=head
        while current!=None:
            if current in J:
                return True
            else:
                J.add(current)
            current=current.next
        return False
