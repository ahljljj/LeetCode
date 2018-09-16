'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

#118 / 118 test cases passed. Runtime: 44 ms
# This running time beats 78.26% of python3 submissions


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        comm = ''
        if n == 0:
            return comm
        elif n == 1:
            return strs[0]
        j = 0
        idx1 = True
        j = 0
        idx = True
        while idx1:
            for i in range(n - 1):
                if strs[i] == '' or strs[i + 1] == '':
                    return comm
                elif strs[i][j] != strs[i + 1][j]:
                    idx = False
                    return comm
            if idx:
                comm += strs[0][j:j + 1]
            else:
                return comm
            j += 1
            for i in range(n):
                if j >= len(strs[i]):
                    return comm
        return comm

