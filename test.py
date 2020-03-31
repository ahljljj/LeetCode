
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


import collections

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        q = collections.deque([root])
        res = [q[0].val]
        while q:
            size = len(q)
            #level = []
            for _ in range(size):
                front = q.popleft()
                if front.left:
                    q.append(front.left)
                    res.append(front.left.val)
                else:
                    res.append('#')
                if front.right:
                    q.append(front.right)
                    res.append(front.right.val)
                else:
                    res.append('#')
        while res and res[-1] == '#':
            res.pop()
        return res

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if not data: return None
        nodes = collections.deque([TreeNode(x) if x != '#' else '#' for x in data])
        #print(nodes)
        q = collections.deque([nodes.popleft()])
        root = q[0]
        while q:
            front = q.popleft()
            left = nodes.popleft() if nodes else None
            right = nodes.popleft() if nodes else None
            if left == '#': left = None
            if right == '#': right = None
            front.left, front.right = left, right
            #print(front.val, left.val if left else None, right.val if right else None)
            if left: q.append(left)
            if right: q.append(right)
        return root

x = [3, 9, 20, '#', '#',15,7]

#x= [3, 9, 20, 15, 7]

S = Solution()
encode = S.deserialize(x)
print("decode: ", S.serialize(encode))