/*

624. Maximum Distance in Arrays


Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].


*/

// cpp, dynamic programming?

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int res = 0, l = arrays[0].front(), r = arrays[0].back();
        for (int i = 1; i < arrays.size(); ++i){
            res = max(res, max(abs(arrays[i].back() - l), abs(arrays[i].front() - r)));
            l = min(l, arrays[i].front());
            r = max(r, arrays[i].back());
        }
        return res;

    }
};