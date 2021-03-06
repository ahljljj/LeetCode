"""
210. Course Schedule II


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        for (x, y) in prerequisites:
            graph[x].append(y)
        res = []
        for i in range(numCourses):
            if self.dfs(graph, i, visit, res) == False:
                return []
        return res

    def dfs(self, graph, course, visit, res):
        if visit[course] == -1:
            return False
        if visit[course] == 1:
            return True
        visit[course] = -1
        for i in graph[course]:
            if self.dfs(graph, i, visit, res) == False:
                return False
        visit[course] = 1
        res.append(course)
        return True

# cpp, dfs, rewrite

'''
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int> res;
        vector<vector<int>> g(numCourses);
        for(auto &p: prerequisites){
            g[p.first].push_back(p.second);
        }
        vector<int> visited(numCourses);
        for (int i = 0; i < numCourses; ++i){
            if (dfs(g, i, visited, res) == false) return {};
        }
        return res;        
    }
    
    bool dfs(vector<vector<int>> &g, int course, vector<int> &visited, vector<int> &res){
        if (visited[course] == -1) return false;
        if (visited[course] == 1) return true;
        visited[course] = -1;
        for (int &i: g[course]){
            if (dfs(g, i, visited, res) == false) return false;
        }
        visited[course] = 1;
        res.push_back(course);
        return true;
    } 
};
'''

# 2020/04/01, topological sorting

'''
Runtime: 100 ms, faster than 84.38% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.3 MB, less than 60.71% of Python3 online submissions for Course Schedule II.
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = self.get_in_degree(numCourses, prerequisites)
        neighbors = self.get_neighbors(numCourses, prerequisites)
        start = [x for x in range(numCourses) if in_degree[x] == 0]
        res = []
        q = collections.deque(start)
        while q:
            front = q.popleft()
            res.append(front)
            for nei in neighbors[front]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0: q.append(nei)
        return res if len(res) == numCourses else []

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