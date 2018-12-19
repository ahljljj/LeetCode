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