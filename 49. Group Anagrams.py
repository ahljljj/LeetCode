"""
49. Group Anagrams


Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.




"""

'''
Time limit exceeded

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def ht(strs):
            dt = {}
            if strs == '': return {'':1}
            for s in strs:
                if s not in dt:
                    dt[s] = 1
                else:
                    dt[s] += 1
            return dt
        res = []
        used = False
        for str1 in strs:
            if not res: 
                res.append([str1])
                continue
            for idx, tmp in enumerate(res):
                if ht(str1) == ht(tmp[0]):
                    res[idx].append(str1)
                    used = True
                    break
            if not used: res.append([str1])
            used = False
        return res
            
        
'''


# not my idea

class Solution:
    def groupAnagrams(self, strs):
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tmp = ''
            for c in count:
                tmp += str(c)
            if tmp not in ans:
                ans[tmp] = [s]
            else:
                ans[tmp].append(s)
        return [l for l in ans.values()]
+

# python, sorted tuple

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in h:
                h[key] = [s]
            else:
                h[key].append(s)
        res = []
        for key, val in h.items():
            res.append(val)
        return res


#cpp, rewrite

'''
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> m;
        for (string & str: strs){
            vector<int> key(26);
            for (char &ch: str) ++key[ch - 'a'];
            m[key].push_back(str);
        }
        vector<vector<string>> res;
        for (auto itr = m.begin(); itr != m.end(); ++itr){
            res.push_back(itr->second);
        }
        return res;
        
    }
};
'''


# 2020/04/29, hashtable

'''
Runtime: 108 ms, faster than 61.93% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.5 MB, less than 30.19% of Python3 online submissions for Group Anagrams.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_sorted = collections.defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            key_to_sorted[key].append(str)
        res = []
        for _, sublist in key_to_sorted.items():
            res.append(sublist)
        return res

