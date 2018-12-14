'''
293. Flip Game


You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output:
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].


'''

# sliding window

class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        w = "--"
        res = []
        for i in range(len(s) - 1):
            if s[i: i + 2] == "++":
                res.append(s[0:i] + w + s[i + 2:])
        return res

# C++, rewrite

'''
class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> res;
        if (s.size() == 0) return res;
        string tmp = s;
        for(int i = 0; i < s.size() - 1; i++){
            if (s.substr(i, 2) == "++") {
                s[i] = '-'; s[i + 1] = '-';
                res.push_back(s);
                s[i] = '+'; s[i + 1] = '+';               
            }
        }
        return res;
        
    }
};

'''

