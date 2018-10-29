/*3. Longest Substring Without Repeating Characters
 * 
 * Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
 * */
 
 // brute force: time complextiy O(n^2)
 
 class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        if (s.empty()) return 0;
        
        int n {s.size()};
        int left {0}, i {0}, j, maxlen {1};
        while (i < s.size() - 1){
            left = i;
            j = i + 1;
            while (j < s.size() && s.substr(left, i - left + 1).find(s[j]) == string::npos){
                i = j;
                j++;                
            }
            maxlen = max(maxlen, j - left);
            i = left + 1;
        }
        return maxlen;       
    }
};


// slide window: time complexity O(n)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        if (s.empty()) return 0;
        unordered_set<char> window;
        int n {s.size()}, i {0}, j {0}, maxlen {1};
        while (i < n && j < n){
            if (window.find(s[j]) == window.end()){
                window.insert(s[j++]);
                maxlen = max(maxlen, j - i);
            } else {
                window.erase(s[i++]);
            }            
        }
        return maxlen;        
    }
};


// hashmap, time complexity: O(n)



class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        if (s.empty()) return 0;
        
        unordered_map<char, int> window;
        
        int n {s.size()}, i {0}, j {0}, maxlen {0}, upper {0};
        
        while (i < n && j < n){
            if (window.find(s[j]) != window.end()){
                i = max(window[s[j]] + 1, i);
            }
            maxlen = max(maxlen, j - i + 1);
            window[s[j]] = j;
            j++;            
        }
        
        return maxlen;
    }
};