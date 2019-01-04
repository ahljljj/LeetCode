/*
709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
*/

// cpp, for loop

class Solution {
public:
    string toLowerCase(string str) {
        for (char &ch: str){
            if (ch >= 'A' && ch <= 'Z') ch = ch - 'A' + 'a';
        }
        return str;

    }
};