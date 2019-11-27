'''
1079. Letter Tile Possibilities

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.



Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188


Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.

'''

'''
2019/11/26, c++, backtracking, fast speed

Runtime: 8 ms, faster than 73.33% of C++ online submissions for Letter Tile Possibilities.
Memory Usage: 8.3 MB, less than 100.00% of C++ online submissions for Letter Tile Possibilities.

class Solution {
public:
    int numTilePossibilities(string tiles) {
        vector<int> count(26, 0);
        for (char &c: tiles) count[c - 'A']++;
        return backtracking(count);
        
    }
    
    int backtracking(vector<int> &count){
        int sum = 0;
        for (int i = 0; i < 26; ++i){
            if (count[i] == 0) continue;
            ++sum;
            count[i]--;
            sum += backtracking(count);
            count[i]++;   
        }
        return sum;
    }
};
'''



'''
2019/11/26, c++, backtracking, simple idea but flow

Runtime: 168 ms, faster than 7.51% of C++ online submissions for Letter Tile Possibilities.
Memory Usage: 17.5 MB, less than 100.00% of C++ online submissions for Letter Tile Possibilities.

class Solution {
public:
    int numTilePossibilities(string tiles) {
        set<string> res;
        string curr = "";
        unordered_map<int, bool> visited;
        backtracking(tiles, res, curr, visited);
        return res.size() - 1;
        
    }
    
    void backtracking(string tiles, set<string> &res, string curr, unordered_map<int, bool> &visited){
        res.insert(curr);
        for (int i = 0; i < tiles.size(); ++i){
            if (visited[i] == true) continue;
            curr += tiles[i];
            visited[i] = true;
            backtracking(tiles, res, curr, visited);
            curr.pop_back();
            visited[i] = false;
        }
    }
};
'''