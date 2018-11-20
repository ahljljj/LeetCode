"""
430. Flatten a Multilevel Doubly Linked List


You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL


Explanation for the above example:

Given the following multilevel doubly linked list:




We should return the following flattened doubly linked list:


"""

# recursion

'''
// flattentail: flatten the node "head" and return the tail in its child (if exists)
    // the tail means the last node after flattening "head"

    // Five situations:
    // 1. null - no need to flatten, just return it
    // 2. no child, no next - no need to flatten, it is the last element, just return it
    // 3. no child, next - no need to flatten, go next
    // 4. child, no next - flatten the child and done
    // 5. child, next - flatten the child, connect it with the next, go next

'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.dfs(head)
        return head

    def dfs(self, head):
        if not head:
            return head
        if not head.child:
            if not head.next:
                return head
            return self.dfs(head.next)
        else:
            nxt = head.next
            child = head.child
            head.next = child
            child.prev = head
            head.child = None
            childtail = self.dfs(child)
            if nxt:
                childtail.next = nxt
                nxt.prev = childtail
                return self.dfs(nxt)
            return childtail








