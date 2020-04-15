'''
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
Accepted
211,009
Submissions
698,112

'''


# 2020/04/15, memoization, too hard

'''
Runtime: 48 ms, faster than 53.43% of Python3 online submissions for Word Break II.
Memory Usage: 14.2 MB, less than 6.90% of Python3 online submissions for Word Break II.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        self.dfs(s, wordDict, 0, memo)
        return memo[0]

    def dfs(self, source, wordDict, pos, memo):
        if pos in memo: return memo[pos]
        if pos == len(source):
            memo[pos] = [""]
            return memo[pos]
        subset = []
        for i in range(pos, len(source)):
            prefix = source[pos: i + 1]
            if prefix not in wordDict: continue
            sub_str = self.dfs(source, wordDict, i + 1, memo)
            for word in sub_str:
                subset.append(prefix + " " + word if word else prefix)
        memo[pos] = subset
        return memo[pos]

