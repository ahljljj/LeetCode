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

#cpp, rewrite, dfs

'''
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
    unordered_map<RandomListNode*,RandomListNode*> m;
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head == nullptr) return head;
        if (m.find(head) != m.end()) return m[head];
        RandomListNode* node = new RandomListNode(head->label); 
        m[head] = node;
        node->next = copyRandomList(head->next);
        node->random = copyRandomList(head->random);
        return node;
        
    }
};
'''


# 2020/04/29, similar to lc 133

'''
Runtime: 36 ms, faster than 60.71% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        copy = self.make_copy(head)
        dummy = head
        while head:
            if head.random: copy[head].random = copy[head.random]
            if head.next: copy[head].next = copy[head.next]
            head = head.next
        return copy[dummy]

    def make_copy(self, head):
        m = {}
        while head:
            m[head] = Node(head.val)
            head = head.next
        return m