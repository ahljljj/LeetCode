'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


Accepted
508,339
Submissions
1,605,714

'''

# 2020/04/28, linked list + hashtable, too hard

'''
Runtime: 212 ms, faster than 59.80% of Python3 online submissions for LRU Cache.
Memory Usage: 22.9 MB, less than 6.06% of Python3 online submissions for LRU Cache.
'''

class ListNode:
    def __init__(self, val):
        self.key = None
        self.val = val
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.stream = {}
        self.capacity = capacity
        self.dummy = ListNode(None)
        self.tail = self.dummy

        # delete head

    # change dummy -> head ->...
    # to dummy -> head.next ->...
    def popleft(self):
        head = self.dummy.next
        new_head = head.next
        self.dummy.next = new_head
        del self.stream[head.key]
        self.stream[new_head.key] = self.dummy

    # append node to the tail of the list
    def append(self, node):
        self.stream[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    # reorganize: change -> node ->...tail
    # to ...tail -> node
    def kick(self, prev):
        node = prev.next
        if self.tail == node:
            return
        prev.next = node.next
        self.stream[node.next.key] = prev
        node.next = None
        self.append(node)

    def get(self, key: int) -> int:
        # print([self.stream[x].val for x in self.stream])
        if key not in self.stream:
            return -1
        prev = self.stream[key]
        node = prev.next
        self.kick(prev)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.stream:
            prev = self.stream[key]
            self.kick(prev)
            prev = self.stream[key]
            node = prev.next
            node.val = value
            return
        node = ListNode(value)
        node.key = key
        self.append(node)
        if len(self.stream) > self.capacity:
            self.popleft()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)