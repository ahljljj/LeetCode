"""
332. Reconstruct Itinerary


Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

'''
wrong

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        res = ['JFK']
        for start, end in tickets:
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)
        start = 'JFK'
        queue = graph['JFK']
        while queue:
            end = min(queue)
            graph[start].remove(end)
            start = end
            res.append(end)
            if end not in graph:
                return res
            queue = graph[end]
        return res



'''


'''
time limit exceeded

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        self.res = ['JFK']
        for start, end in tickets:
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)
        for key in graph:
            graph[key].sort()
        self.helper(graph, 'JFK', ['JFK'])
        
        return self.res
    
    def helper(self, graph, start, tmp):
        # edge case
        if (start not in graph) or (not graph[start]):
            if len(tmp) > len(self.res):
                self.res = tmp[:]
            return
        queue = graph[start][:]
        for end in queue:
            tmp.append(end)
            graph[start].remove(end)
            self.helper(graph, end, tmp)
            graph[start].append(end)
            tmp.pop()
        
'''





'''
intuition

I use a dictionary to represent the tickets (start -> [list of possible destinations]). Then, I start the route at JFK and I dfs from there. Since I do the dfs in sorted order, the first time that I find a possible route, I can return it and know that it is in the smallest lexigraphic order. Finally, note that the worked variable either contains None (as a result of a failed search) or the correct route.


'''


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        self.res = ['JFK']
        self.ind = False
        for start, end in tickets:
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)
        # sort the neighbors
        for key in graph:
            graph[key].sort()
        n = len(tickets)
        return self.helper(graph, 'JFK', ['JFK'], n)

    def helper(self, graph, start, tmp, n):
        # edge case: stop when there is no neighbor or all neighbors have been used
        if (start not in graph) or (not graph[start]):
            if len(tmp) == n + 1:
                self.res = tmp[:]
                return self.res
            return
        # create a shallow copy of neighbors
        neighbors = graph[start][:]
        #        neighbors = sorted(graph[start])
        for end in neighbors:
            tmp.append(end)
            graph[start].remove(end)
            find = self.helper(graph, end, tmp, n)
            # stop at the first time we reach all cities since we have already sorted
            if find:
                return self.res
            graph[start].append(end)
            tmp.pop()