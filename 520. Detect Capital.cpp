/*
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

*/

//cpp, unordered_set

class Solution {
public:
    bool detectCapitalUse(string word) {
        unordered_set<char> aaa, AAA;
        for (char a = 'a'; a <= 'z'; ++a){
            aaa.insert(a);
            AAA.insert(a - 'a' + 'A');
        }
        bool id1 = false, id2 = false;
        for (int i = 1; i < word.length(); ++i){
           if (aaa.find(word[i]) != aaa.end()) id1 = true;
            if (AAA.find(word[i]) != AAA.end()) id2 = true;
            if (id1 && id2) return false;
        }
        if (id2 && AAA.find(word[0]) == AAA.end()) return false;
        return true;
    }
};