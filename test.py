'''
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> table =  {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res;
        for (char digit : digits){
            cout << digit << endl;
            int idx = digit - '0' - 2;
            for (char ch: table[idx]){
                if (!res.empty()){
                    for (string s: res) s += ch;
                } else res.push_back(ch);
            }
        }
        return res;

    }
};c


'''