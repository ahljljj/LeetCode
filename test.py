class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.visited = set()
        self.dummy = ListNode(None)
        self.tail = self.dummy
        self.key_to_prev = {}

    def popleft(self):
        head = self.dummy.next
        self.dummy.next = head.next

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        # write your code here
        if num in self.visited:
            if num not in self.key_to_prev: return
            prev = self.key_to_prev[num]
            node = prev.next
            prev.next = node.next
            self.key_to_prev[node.next.val] = prev
            return
        node = ListNode(num)
        self.key_to_prev[num] = self.tail
        self.tail.next = node
        self.visited.add(node)

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
        # write your code here
        head = self.dummy.next
        return head.val

ds = DataStream()
ds.add(1)
print(ds.firstUnique())