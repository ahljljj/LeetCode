'''
547. Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
Accepted
140,757
Submissions
246,676

'''

'''
2020/04/05, union find

Runtime: 388 ms, faster than 6.25% of Python3 online submissions for Friend Circles.
Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Friend Circles.

'''


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        m = len(M)
        union_find = UnionFind(m)
        for i in range(m):
            for j in range(m):
                if i != j and M[i][j]:
                    union_find.union(i, j)
        friend_circles = set()
        for x in range(m):
            # should be union_find.find(x)
            # common mistake by using union_find.parents[x]
            friend_circles.add(union_find.find(x))
        return len(friend_circles)


class UnionFind:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, A):
        root = A
        while root != self.parents[root]:
            root = self.parents[root]
        while A != root:
            old_root = self.parents[A]
            self.parents[A] = root
            A = old_root
        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY: return
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]