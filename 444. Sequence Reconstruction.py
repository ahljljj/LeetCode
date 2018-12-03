"""
444. Sequence Reconstruction


Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.


"""

# topological sort
'''

The basic is to get topological sort of seqs nodes, if it is unique and equal to org, then true, else False

Following is how to implement in details:

in each step,
if we have more than one node whose incoming nodes count is zero then org is not unique, return False

At last we check if the topological sort contain all nodes in the in seqs and equal to org
'''

class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        seqs = [seq for seq in seqs if seq]
        if not seqs:
            return False
        freq = [0] * (1 + len(org))
        neighbor = {}
        # initialize head and neightbor
        for seq in seqs:
            if seq[0] > len(org) or seq[0] < 0:
                return False
            for i in range(len(seq) - 1):
                if seq[i + 1] > len(org) or seq[i + 1] < 0:
                    return False
                freq[seq[i + 1]] += 1
                neighbor[seq[i]] = neighbor.get(seq[i], []) + [seq[i + 1]]
        heads = [i for i in range(1, len(freq)) if freq[i] == 0]
        res = []
        while len(heads) == 1:
            head = heads.pop()
            res.append(head)
            if head not in neighbor:
                break
            for node in neighbor[head]:
                freq[node] -= 1
                if freq[node] == 0:
                    heads.append(node)
                if len(heads) > 1: return False
        return res == org

