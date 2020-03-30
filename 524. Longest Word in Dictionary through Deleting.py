'''
524. Longest Word in Dictionary through Deleting

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

2020/03/29, sort with comparator

'''


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        key = functools.cmp_to_key(self.cmp)
        d.sort(key=key, reverse=True)
        for t in d:
            if self.is_substr(t, s):
                return t
        return ""

    def is_substr(self, target, s):
        # detect if target is a subsring of s
        i, j = 0, 0
        while i < len(target) and j < len(s):
            if target[i] == s[j]:
                i += 1
            j += 1
        return i == len(target)

    def cmp(self, x, y):
        if len(x) != len(y):
            return len(x) - len(y)
        elif x > y:
            return -1
        elif x < y:
            return 1
        else:
            return 0