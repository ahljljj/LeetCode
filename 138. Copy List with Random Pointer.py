"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return head
        old = head
        new = RandomListNode(old.label)
        self.visited[old] = new
        while old:
            new.random = self.clonenode(old.random)
            new.next = self.clonenode(old.next)
            new = new.next
            old = old.next
        return self.visited[head]

    def clonenode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return None