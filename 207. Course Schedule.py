"""
207. Course Schedule


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        # initialize graph
        for course, pre in prerequisites:
            graph[course].append(pre)
        for i in range(numCourses):
            if self.dfs(graph, visit, i) == False:
                return False
        return True

    def dfs(self, graph, visit, course):
        # if the course is the one we are visiting, then there is a cycle
        # remeber that we consider the inverse ordering
        if visit[course] == -1:
            return False
        if visit[course] == 1:
            return True
        visit[course] = -1
        for pre in graph[course]:
            if self.dfs(graph, visit, pre) == False:
                return False
        visit[course] = 1
        return True
