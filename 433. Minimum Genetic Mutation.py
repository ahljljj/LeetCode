"""
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.


Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1


Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2


Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3


"""

# standard bfs

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = [start]
        bank = set(bank)
        replace = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        used = set()
        count = 0
        while queue:
            tmp = set()
            count += 1
            for node in queue:
                used.add(node)
                for i in range(len(node)):
                    for j in range(len(replace)):
                        if replace[j] == node[i]:
                            continue
                        nxt = node[:i] + replace[j] + node[i + 1:]
                        if nxt in bank:
                            if nxt == end:
                                return count
                            if nxt not in used:
                                tmp.add(nxt)
            queue = tmp

        return -1



