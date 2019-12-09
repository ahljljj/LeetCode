"""
320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

# cpp, bit manipulation

'''
class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        for (int i = 0; i <  (1 << word.length()); ++i)
            res.push_back(abbr(word, i));        
        return res;        
    }
    
    string abbr(string word, int num){
        int k = 0;
        string res;
        for (int i = 0; i < word.length(); ++i, num >>= 1){
            if ( (num & 1) == 0 ){
                if (k != 0) {
                    res += to_string(k);
                    k = 0;
                }
                res += word[i];
            } else
                ++k;
        }
        if (k != 0) res += to_string(k);
        return res;
        
    }
};

'''

# cpp, dfs

'''
class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        dfs(res, word, 0, "", 0);
        return res;
        
    }
    
    void dfs(vector<string> &res, string word, int idx, string curr, int count){
        // Once we reach the end, append current to the result
        if (word.size() == idx) 
            res.push_back( curr + (count > 0 ? to_string(count) : ""));
        else{
            // Skip current position, and increment count
            dfs(res, word, idx + 1, curr, count + 1);
            // Include current position, and zero-out count
            dfs(res, word, idx + 1, curr + (count > 0? to_string(count) : "") + word[idx],0);           
        }
            
        
        
    }
};

'''





'''
2019/12/08, c++, dfs

Runtime: 52 ms, faster than 87.28% of C++ online submissions for Generalized Abbreviation.
Memory Usage: 23.4 MB, less than 25.00% of C++ online submissions for Generalized Abbreviation.


class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        string curr;
        dfs(res, word, curr, 0, 0);
        return res;        
    }
    
    void dfs(vector<string> &res, string &word, string curr, int pos, int count){
        if (pos == word.size()){
            if (count > 0) curr += to_string(count);
            res.push_back(curr);
            return;
        }
        dfs(res, word, curr + (count > 0 ? to_string(count) : "") + word[pos], pos + 1, 0);
        dfs(res, word, curr, pos + 1, count + 1);
        //return;
    }
};
'''