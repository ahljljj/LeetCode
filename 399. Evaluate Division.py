"""
399. Evaluate Division


Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.



"""

# bfs + graph: ridiculous slow


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        eqns = {}
        for (eq, val) in zip(equations, values):
            if eq[0] not in eqns:
                eqns[eq[0]] = {eq[1]: val}
            else:
                eqns[eq[0]][eq[1]] = val
            if eq[1] not in eqns:
                eqns[eq[1]] = {eq[0]: 1 / val}
            else:
                eqns[eq[1]][eq[0]] = 1 / val
        self.eqns = eqns
        visited = {}
        for key in eqns:
            visited[key] = False
        tmp = copy.deepcopy(visited)
        res = []
        for query in queries:
            res.append(self.helper(1, query[0], query[1], tmp))
            tmp = copy.deepcopy(visited)

        return res

    def helper(self, res, start, end, visited):
        if start not in self.eqns or end not in self.eqns:
            return -1
        if end in self.eqns[start]:
            return self.eqns[start][end]
        nxt = self.eqns[start]
        visited[start] = True
        flag = False
        for eq in nxt:
            if not visited[eq]:
                tmp = self.helper(res, eq, end, visited)
                if tmp != -1:
                    res = nxt[eq] * tmp
                    flag = True
                    break
        return res if flag else -1

# modified dfs


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        eqns = {}
        for (eq, val) in zip(equations, values):
            if eq[0] not in eqns:
                eqns[eq[0]] = {eq[1]: val}
            else:
                eqns[eq[0]][eq[1]] = val
            if eq[1] not in eqns:
                eqns[eq[1]] = {eq[0]: 1 / val}
            else:
                eqns[eq[1]][eq[0]] = 1 / val
        self.eqns = eqns
        visited = set()
        res = []
        for query in queries:
            res.append(self.helper(1, query[0], query[1], visited))
            visited = set()
        return res

    def helper(self, res, start, end, visited):
        if start not in self.eqns or end not in self.eqns:
            return -1
        if end in self.eqns[start]:
            return self.eqns[start][end]
        nxt = self.eqns[start]
        visited.add(start)
        for eq in nxt:
            if eq not in visited:
                tmp = self.helper(res, eq, end, visited)
                if tmp != -1:
                    res = nxt[eq] * tmp
                    return res
        return -1



# use collections.defaultdict: codes become shorter but slower

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        eqns = collections.defaultdict(dict)
        for (eq, val) in zip(equations, values):
            eqns[eq[0]][eq[1]] = val
            eqns[eq[1]][eq[0]] = 1 / val
        self.eqns = eqns
        visited = set()
        res = []
        for query in queries:
            res.append(self.helper(1, query[0], query[1], visited))
            visited = set()
        return res

    def helper(self, res, start, end, visited):
        if start not in self.eqns or end not in self.eqns:
            return -1
        if end in self.eqns[start]:
            return self.eqns[start][end]
        nxt = self.eqns[start]
        visited.add(start)
        for eq in nxt:
            if eq not in visited:
                tmp = self.helper(res, eq, end, visited)
                if tmp != -1:
                    res = nxt[eq] * tmp
                    return res
        return -1


# union find

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.parents = {}
        self.weights = {}
        self.rank = {}

        for (numerator, denominator), val in zip(equations, values):
            if numerator not in self.parents:
                self.parents[numerator] = numerator
                self.weights[numerator] = 1.0
                self.rank[numerator] = 1
            if denominator not in self.parents:
                self.parents[denominator] = denominator
                self.weights[denominator] = 1.0
                self.rank[denominator] = 1
            self.union(numerator, denominator, val)
        res = []
        for (u, v) in queries:
            if u not in self.parents or v not in self.parents:
                res.append(-1.0)
            else:
                p1, p2 = self.find(u), self.find(v)
                if p1 != p2:
                    res.append(-1.0)
                else:
                    res.append(self.weights[u] / self.weights[v])
        return res

    def find(self, node):  # rank donot need updated
        if node != self.parents[node]:
            p = self.parents[node]
            self.parents[node] = self.find(p)
            self.weights[node] *= self.weights[p]
        return self.parents[node]

    def union(self, u, v, val):
        p1 = self.find(u)
        p2 = self.find(v)
        if self.rank[p1] > self.rank[p2]:  # parent is the denominator, weight is the corresponding fraction value
            p1, p2 = p2, p1
            val = 1 / val
            u, v = v, u
        if p1 != p2:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
            #            self.rank[p1] = 1 # p1 is not a root any more, the rank is not important
            self.weights[p1] = self.weights[v] / self.weights[u] * val


'''
2020/04/06, union find, too hard, a reorganziation of the old codes

Runtime: 24 ms, faster than 90.87% of Python3 online submissions for Evaluate Division.
Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for Evaluate Division.

'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # initialize the nodes for the graph
        nodes = set()
        for eqn in equations:
            for c in eqn:
                nodes.add(c)
        union_find = UnionFind(nodes)
        for ((x, y), w) in zip(equations, values):
            union_find.union(x, y, w)
        res = []
        for (x, y) in queries:
            if x not in nodes or y not in nodes \
                    or union_find.find(x) != union_find.find(y):
                res.append(-1.0)
                continue
            res.append(union_find.weight[x] / union_find.weight[y])
        return res


class UnionFind:
    def __init__(self, nodes):
        # for a fraction, denominator is the farther of numerator
        # for example, a / b ---> parents[a] = b
        self.parents = {x: x for x in nodes}
        # weight is distance between numerator and denominator
        # for example, weight[a] = value (a / parents[a])
        self.weight = {x: 1 for x in nodes}
        # path compression
        self.size = {x: 1 for x in nodes}

    def find(self, A):
        # use DFS to update the weights along the path
        if A != self.parents[A]:
            curr_root = self.parents[A]
            self.parents[A] = self.find(curr_root)
            self.weight[A] *= self.weight[curr_root]
        return self.parents[A]

    def union(self, x, y, w):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            self.weight[rootX] = self.weight[y] / self.weight[x] * w
        else:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.weight[rootY] = self.weight[x] / self.weight[y] * (1 / w)








