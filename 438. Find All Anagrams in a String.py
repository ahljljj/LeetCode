"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


"""


# sliding window O(k + n)

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)
        p = self.hashmap(p)
        curr = self.hashmap(s[0:m])
        res = []
        for i in range(n - m + 1):
            if curr == p:
                res.append(i)
            curr[s[i]] -= 1
            if curr[s[i]] == 0:
                curr.pop(s[i], None)
            if i + m < n: curr[s[i + m]] = curr.get(s[i + m], 0) + 1
        return res

    def hashmap(self, s):
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        return d
