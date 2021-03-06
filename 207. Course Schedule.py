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

# cpp, backtracking, rewrite

'''
class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> visited(numCourses);
        for (auto &p: prerequisites){
            g[p.first].push_back(p.second);
        }
        for (int i = 0; i < numCourses; ++i){
            if (!dfs(g, visited, i)) return false;
        }
        return true;
        
    }
    
    bool dfs(vector<vector<int>> &g, vector<int> &visited, int i){
        if (visited[i] == -1) return false;
        if (visited[i] == 1) return true;
        visited[i] = -1;
        for (int &n: g[i]){
            if (!dfs(g, visited, n)) return false;
        }
        visited[i] = 1;
        return true;
    }
};
'''


# 2020/04/01, BFS on graph

'''
Runtime: 88 ms, faster than 98.94% of Python3 online submissions for Course Schedule.
Memory Usage: 15.4 MB, less than 65.31% of Python3 online submissions for Course Schedule.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = self.get_in_degree(numCourses, prerequisites)
        neighbors = self.get_neighbors(numCourses, prerequisites)
        start = [x for x in range(numCourses) if in_degree[x] == 0]
        res = 0
        q = collections.deque(start)
        while q:
            front = q.popleft()
            res += 1
            for nei in neighbors[front]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0: q.append(nei)
        return res == numCourses

    def get_in_degree(self, n, graph):
        # course #: 0, 1,..., n - 1
        # if (course, pre_course) in graph,
        # then add 1 to the in degree of this course
        m = [0] * n
        for (course, _) in graph:
            m[course] += 1
        return m

    def get_neighbors(self, n, graph):
        # course #: 0, 1, ..., n - 1
        # for each course, get all down stream courses
        m = {x: [] for x in range(n)}
        for (course, pre_course) in graph:
            m[pre_course].append(course)
        return m
