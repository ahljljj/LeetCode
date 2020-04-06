'''
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
Accepted
64,771
Submissions
140,024

'''

'''
2020/04/05, union find, no that elegant

Runtime: 516 ms, faster than 13.11% of Python3 online submissions for Accounts Merge.
Memory Usage: 19 MB, less than 44.44% of Python3 online submissions for Accounts Merge.

'''


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes = []
        # initialze the graph
        for account in accounts:
            for i in range(1, len(account)):
                nodes.append((account[0], account[i]))
        union_find = UnionFind(nodes)
        # build parent - kid relation according to the accounts
        for account in accounts:
            name, email = account[0], account[1]
            acc1 = (name, email)
            for i in range(2, len(account)):
                acc2 = (name, account[i])
                union_find.union(acc1, acc2)
        # find all the kids for a parent
        m = {x: set() for x in nodes}
        for node in nodes:
            p = union_find.find(node)
            m[p].add(node)
        res = []
        # reconstruct the accounts using sorting
        for x in m:
            if not m[x]: continue
            tmp = [x[0]]
            for kid in m[x]:
                tmp.append(kid[1])
            tmp.sort()
            res.append(tmp)
        return res


class UnionFind:
    def __init__(self, nodes):
        self.parents = {x: x for x in nodes}
        self.size = {x: 1 for x in nodes}

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
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]

