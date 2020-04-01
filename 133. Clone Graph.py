"""
133. Clone Graph

Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.


OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.


As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.


Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
Note: The information about the tree serialization is only meant so that you can understand error output if you get a wrong answer. You don't need to understand the serialization to solve the problem.


"""


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node

        queue = [node]
        copyNode = UndirectedGraphNode(node.label)
        dic = {}
        dic[node] = copyNode
        while len(queue) > 0:
            curr = queue.pop(0)
            for nd in curr.neighbors:
                if nd in dic:
                    dic[curr].neighbors.append(dic[nd])
                else:
                    ndCopy = UndirectedGraphNode(nd.label)
                    dic[nd] = ndCopy
                    dic[curr].neighbors.append(ndCopy)
                    queue.append(nd)

        return dic[node]


# 2020/04/01, BFS

'''
Runtime: 36 ms, faster than 67.96% of Python3 online submissions for Clone Graph.
Memory Usage: 14 MB, less than 48.15% of Python3 online submissions for Clone Graph.
'''


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        # get all nodes of the graph
        nodes = self.get_nodes(node)
        # deep copy all nodes
        m = {}
        for nd in nodes:
            m[nd] = Node(nd.val)
        # deep copy all neighbors/edges
        for nd in nodes:
            nd_copy = m[nd]
            for nei in nd.neighbors:
                nei_copy = m[nei]
                nd_copy.neighbors.append(nei_copy)
        return m[node]

    def get_nodes(self, node: 'Node'):
        if not node: return set()
        q = collections.deque([node])
        res = set()
        while q:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                if front in res: continue
                res.add(front)
                for nei in front.neighbors:
                    q.append(nei)
        return res