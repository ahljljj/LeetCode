"""
311. Sparse Matrix Multiplication


Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |


"""

# python, double hashtable

'''
The idea is to preprocess matrix to be sparse representation, which is efficient for computing.

We can write matrix as pairs of (i, A[i][j]) or (j, A[i][j]). If we decide to write a matrix as (i, A[i][j]), we will need j rows, each row j represents all elements coming from A's jth row.
If we represent A and B in (i, A[i][j]), (j, B[i][j]), we just need to compute row by row, and in each row calculation we only need to find elements with the same index.

The overall time complexity is O(N^2*K), where K is the number of non-zero elements.

'''

class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        n, k = len(A), len(A[0])
        m = len(B[0])
        vA = [dict() for i in range(n)]
        vB = [dict() for i in range(m)]
        for i in range(n):
            for j in range(k):
                if A[i][j]: vA[i][j] = A[i][j]
        for i in range(k):
            for j in range(m):
                if B[i][j]: vB[j][i] = B[i][j]
        res = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                for r in vA[i]:
                    if r in vB[j]:
                        res[i][j] += vA[i][r] * vB[j][r]
        return res