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

# cpp, rewrite

'''
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        int n = A.size(), k = A[0].size(), m = B[0].size();
        vector<unordered_map<int, int> > vA(n);
        vector<unordered_map<int, int> > vB(m);
        for (int i = 0; i < n; i ++){
            for (int j = 0; j < k; j++){
                if (A[i][j]) vA[i][j] = A[i][j];
            }
        }
        for (int i = 0; i < k; i ++){
            for (int j = 0; j < m; j++){
                if (B[i][j]) vB[j][i] = B[i][j];
            }
        }
        vector<vector<int>> res(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                for (auto r: vA[i]){
                    if (vB[j].find(r.first) != vB[j].end())
                        res[i][j] += vA[i][r.first] * vB[j][r.first];
                }
            }
        }
        return res;
        
    }
};

'''

# 2020/05/11, hashmap

'''
Runtime: 60 ms, faster than 65.30% of Python3 online submissions for Sparse Matrix Multiplication.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Sparse Matrix Multiplication.
'''


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        k, m = len(B), len(B[0])
        res = [[0] * m for _ in range(n)]
        m_A = self.make_row_vec(A)
        m_B = self.make_col_vec(B)
        for i in range(n):
            for j in range(m):
                res[i][j] = self.vec_prod(m_A[i], m_B[j])
        return res

    def make_row_vec(self, matrix):
        n, m = len(matrix), len(matrix[0])
        res = [{} for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    res[i][j] = matrix[i][j]
        return res

    def make_col_vec(self, matrix):
        n, m = len(matrix), len(matrix[0])
        res = [{} for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    res[j][i] = matrix[i][j]
        return res

    def vec_prod(self, x, y):
        res = 0
        for n in x:
            if n in y:
                res += x[n] * y[n]
        return res


# 2020/05/11, no hashtable

'''
Runtime: 60 ms, faster than 65.30% of Python3 online submissions for Sparse Matrix Multiplication.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Sparse Matrix Multiplication.
'''

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        k, m = len(B), len(B[0])
        res = [[0] * m for _ in range(n)]
        rows_A = self.make_row_vec(A)
        cols_B = self.make_col_vec(B)
        for i in range(n):
            for j in range(m):
                res[i][j] = self.vec_prod(rows_A[i], cols_B[j])
        return res

    def make_row_vec(self, matrix):
        n, m = len(matrix), len(matrix[0])
        res = []
        for i in range(n):
            row = []
            for j in range(m):
                if matrix[i][j]:
                    row.append((j, matrix[i][j]))
            res.append(row)
        return res

    def make_col_vec(self, matrix):
        n, m = len(matrix), len(matrix[0])
        res = []
        for j in range(m):
            col = []
            for i in range(n):
                if matrix[i][j]:
                    col.append((i, matrix[i][j]))
            res.append(col)
        return res

    def vec_prod(self, x, y):
        res = 0
        i1, i2 = 0, 0
        while i1 < len(x) and i2 < len(y):
            if x[i1][0] < y[i2][0]:
                i1 += 1
            elif x[i1][0] > y[i2][0]:
                i2 += 1
            else:
                res += x[i1][1] * y[i2][1]
                i1 += 1;
                i2 += 1
        return res