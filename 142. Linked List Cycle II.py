"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?


"""

'''
extra space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        if head.next == head: return head
        used = [head]
        head = head.next
        while head:
            if head in used:
                return head
                break
            used.append(head)
            head = head.next
        return None
        

'''

# two pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        slow = fast = head
        meet = ListNode(None)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                meet = slow
                break
        while head and meet:
            if head == meet: return meet
            head = head.next
            meet = meet.next

        return None
