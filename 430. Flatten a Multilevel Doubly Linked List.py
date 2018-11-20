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



# stack

'''
Pseudocode
Initialize a current reference to the head of the list and an empty stack
If our current reference is a Node, then see if it has a child.
(case 1) If it does have a next, then push its next reference (if it has one) to the top of the Stack. 
(case 2) If it does have a child, then push its child reference (if it has one) to the top of the Stack. After this operation, the child reference of the current reference should be the top of the Stack, and the top of the Stack's previous reference should be the current reference.
Advance the current reference forward to its next reference.
Repeat 2 and 3 until the current reference is None.

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
        if not head:
            return head
        prev = Node(None, None, head, None)
        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            curr.child = None
            prev = curr
        head.prev = None
        return head








