'''
851. Loud and Rich

In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label x, simply "person x".

We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

Also, we'll say quiet[x] = q if person x has quietness q.

Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.



Example 1:

Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation:
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
Note:

1 <= quiet.length = N <= 500
0 <= quiet[i] < N, all quiet[i] are different.
0 <= richer.length <= N * (N-1) / 2
0 <= richer[i][j] < N
richer[i][0] != richer[i][1]
richer[i]'s are all different.
The observations in richer are all logically consistent.
Accepted
11,550
Submissions
22,834

'''


# 2020/04/26, brute force dfs, barely pass

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = self.make_graph(richer, n)
        answer = []
        for i in range(n):
            self.quietness, self.person = float("inf"), None
            self.dfs(graph, i, quiet, set())
            answer.append(self.person)
        return answer

    def make_graph(self, richer, n):
        # given any node, neighbors are richer than the node
        m = {i: set([i]) for i in range(n)}
        for x, y in richer:
            m[y].add(x)
        return m

    def dfs(self, graph, i, quiet, visited):
        if quiet[i] < self.quietness:
            self.quietness = quiet[i]
            self.person = i
        if i in visited:
            return
        visited.add(i)
        for nei in graph[i]:
            self.dfs(graph, nei, quiet, visited)


# better solution from others

'''
Runtime: 480 ms, faster than 76.52% of Python3 online submissions for Loud and Rich.
Memory Usage: 23.3 MB, less than 100.00% of Python3 online submissions for Loud and Rich.
'''

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = self.make_graph(richer, n)
        answer = [None] * n
        for i in range(n):
            self.dfs(graph, i, quiet, set(), answer)
        return answer

    def make_graph(self, richer, n):
        # given any node, neighbors are richer than the node
        m = collections.defaultdict(set)
        for x, y in richer:
            m[y].add(x)
        return m

    def dfs(self, graph, i, quiet, visited, answer):
        if answer[i]: return answer[i]
        answer[i] = i
        for nei in graph[i]:
            person = self.dfs(graph, nei, quiet, visited, answer)
            if quiet[person] < quiet[answer[i]]:
                answer[i] = person
        return answer[i]



