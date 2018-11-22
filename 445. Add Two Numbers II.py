"""
445. Add Two Numbers II


You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


"""

# stack/ extra space
# time complexity O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nums1, nums2 = [], []
        n1, n2 = 0, 0
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        sum, carry = 0, 0
        head, prev = None, None
        while nums1 or nums2 or carry:
            sum = carry
            if nums1: sum += nums1.pop()
            if nums2: sum += nums2.pop()
            carry = sum // 10
            sum %= 10
            if not prev:
                prev = ListNode(sum)
                continue
            head = ListNode(sum)
            head.next = prev
            prev = head
        return head if head else prev

