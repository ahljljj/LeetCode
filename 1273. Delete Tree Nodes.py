'''
1273. Delete Tree Nodes

A tree rooted at node 0 is given as follows:

The number of nodes is nodes;
The value of the i-th node is value[i];
The parent of the i-th node is parent[i].
Remove every subtree whose sum of values of nodes is zero.

After doing so, return the number of nodes remaining in the tree.



Example 1:



Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2


Constraints:

1 <= nodes <= 10^4
-10^5 <= value[i] <= 10^5
parent.length == nodes
parent[0] == -1 which indicates that 0 is the root.
Accepted
3,831
Submissions
6,119

'''



#2020/04/17, divide and conquer

'''
Runtime: 244 ms, faster than 83.50% of Python3 online submissions for Delete Tree Nodes.
Memory Usage: 25.1 MB, less than 100.00% of Python3 online submissions for Delete Tree Nodes.
'''


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = {i: [] for i in range(nodes)}
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        self.res = 0
        zeros, _, _ = self.div_conq(tree, 0, value)
        return nodes - zeros

    def div_conq(self, tree, node, value):
        if not tree[node]:
            return value[node] == 0, 1, value[node]
        curr_sum = value[node]
        curr_size = 1
        curr_zero = 0
        for kid in tree[node]:
            zero, kid_size, kid_sum = self.div_conq(tree, kid, value)
            curr_zero += zero
            curr_sum += kid_sum
            curr_size += kid_size
        if curr_sum == 0: curr_zero = curr_size
        return curr_zero, curr_size, curr_sum



