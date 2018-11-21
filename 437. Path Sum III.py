"""
437. Path Sum III


You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


"""

# dfs: ridiculous slow
#  traversing same elements multiple times

'''
intuition

for each parent node in the tree, we have 2 choices:
1. include it in the path to reach sum.
2. not include it in the path to reach sum. 

for each child node in the tree, we have 2 choices:
1. take what your parent left you.
2. start from yourself to form the path.

one little thing to be careful:
every node in the tree can only try to be the start point once.

for example, When we try to start with node 1, node 3, as a child, could choose to start by itself.
             Later when we try to start with 2, node 3, still as a child, 
             could choose to start by itself again, but we don't want to add the count to result again.
     1
      \
       2
        \
         3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        self.used = set()
        self.dfs(root, sum, root.val)
        return self.count

    def dfs(self, root, sum, curr):
        if not root:
            return
        if sum == curr:
            self.count += 1
        if root.left:
            self.dfs(root.left, sum, curr + root.left.val)
            if root.left not in self.used:
                self.dfs(root.left, sum, root.left.val)
            self.used.add(root.left)
        if root.right:
            self.dfs(root.right, sum, curr + root.right.val)
            if root.right not in self.used:
                self.dfs(root.right, sum, root.right.val)
            self.used.add(root.right)
        return


# recursion using two functions
# better than my idea (more clear and clean)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        self.helper(root, sum)
        return self.count

    def dfs(self, root, sum):
        if not root:
            return
        if root.val == sum:
            self.count += 1
        if root.left:
            self.dfs(root.left, sum - root.val)
        if root.right:
            self.dfs(root.right, sum - root.val)

    def helper(self, root, sum):
        if not root:
            return
        self.dfs(root, sum)
        if root.left: self.helper(root.left, sum)
        if root.right: self.helper(root.right, sum)


# memo time complexity: O(n)

'''

Two Sum Method: Optimized Solution

A more efficient implementation uses the Two Sum idea. It uses a hash table (extra memory of order N). With more space, it gives us an O(N) complexity.
As we traverse down the tree, at an arbitrary node N, we store the sum until this node N (sum_so_far (prefix) + N.val). in hash-table. Note this sum is the sum from root to N.
Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.We pass in our recursive routine.
How do we know if we have a path of target sum which ends at this grand-child G? Say there are multiple such paths that end at G and say they start at A, B, C where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target. Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement at G as sum_so_far+G.val-target and look up the hash-table for the number of paths which had this sum
Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.memo = {0: 1}
        self.count = 0
        self.dfs(root, 0, sum)
        return self.count

    def dfs(self, root, prev, sum):
        if not root:
            return
        curr = prev + root.val
        tmp = curr - sum
        if tmp in self.memo:
            self.count += self.memo[tmp]
        self.memo[curr] = self.memo.get(curr, 0) + 1
        self.dfs(root.left, curr, sum)
        self.dfs(root.right, curr, sum)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        # it works similar to backtracking, namely you are switching to a new path.
        self.memo[curr] -= 1

