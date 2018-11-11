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



