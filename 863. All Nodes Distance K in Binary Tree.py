'''
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.


'''

'''
2019/11/19, python 3, not my solution

Runtime: 32 ms, faster than 96.82% of Python3 online submissions for All Nodes Distance K in Binary Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for All Nodes Distance K in Binary Tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.findParDFS(root, None)
        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, d + 1))
        return []

    def findParDFS(self, node, par):
        if node:
            node.par = par
            self.findParDFS(node.left, node)
            self.findParDFS(node.right, node)


'''
2019/11/19, python 3, slight modification

Runtime: 36 ms, faster than 90.81% of Python3 online submissions for All Nodes Distance K in Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for All Nodes Distance K in Binary Tree.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.findParDFS(root, None)
        queue = collections.deque([target])
        visited = {target}
        d = 0
        while queue:
            if d == K:
                return [node.val for node in queue]
            breadth = len(queue)
            d += 1
            for i in range(breadth):
                node = queue.popleft()
                for nei in (node.left, node.right, node.par):
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        return []

    def findParDFS(self, node, par):
        if node:
            node.par = par
            self.findParDFS(node.left, node)
            self.findParDFS(node.right, node)