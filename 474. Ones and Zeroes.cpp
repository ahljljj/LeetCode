/*
474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

*/

// cpp, brute force, tle

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int maxLen = 0;
        for (int i = 0; i < (1 << strs.size()); ++i){
            int currLen = 0, ones = 0, zeros = 0;
            for (int j = 0; j < strs.size(); ++j){
                if ((i & (1 << j)) != 0){
                    vector<int> tmp = counting(strs[j]);
//                    cout << tmp[0] << " " << tmp[1] << endl;
                    ones += tmp[1];
                    zeros += tmp[0];
                    ++currLen;
                }
            }
            if (zeros <= m && ones <= n) maxLen = max(maxLen, currLen);

        }
        return maxLen;

    }

    vector<int> counting(string & str){
        vector<int> res = {0, 0};
        for (int i = 0; i < str.size(); ++i) ++res[str[i] - '0'];
//        cout << res[0] << " " << res[1] << endl;
        return res;
    }
};