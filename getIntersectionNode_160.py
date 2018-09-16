'''

160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''



#42 / 42 test cases passed. Runtime: 276 ms
#Your runtime beats 9.15% of python 3 submissons.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        J = set()
        while headA and headB:
            J.add(headA)
            if headB in J:
                return headB
            else:
                J.add(headB)
            headA = headA.next
            headB = headB.next
            while headA:
                if headA in J:
                    return headA
                else:
                    J.add(headA)
                headA = headA.next
            while headB:
                if headB in J:
                    return headB
                else:
                    J.add(headB)
                headB = headB.next
        return None
