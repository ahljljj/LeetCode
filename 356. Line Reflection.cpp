/*
356. Line Reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false
Follow up:
Could you do better than O(n2) ?



*/

// cpp, hash table

/*
The idea is quite simple. If there exists a line reflecting the points, then each pair of symmetric points will have their x coordinates adding up to the same value, including the pair with the maximum and minimum x coordinates. So, in the first pass, I iterate through the array, adding each point to the hash set, and keeping record of the minimum and maximum x coordinates. Then, in the second pass, I check for every point to the left of the reflecting line, if its symmetric point is in the point set or not. If all points pass the test, then there exists a reflecting line. Otherwise, not.

By the way, here, to hash the content of an array, rather than the reference value, I use Arrays.hashCode(int[]) first, and then re-hash this hash code. You can also use Arrays.toString(int[]) to first convey the 2d array to a string, and then hash the string. But the second method is slower.
*/

class Solution {
public:
    bool isReflected(vector<pair<int, int>>& points) {
        set<pair<int,int>> s(points.begin(), points.end());
        int lower = INT_MAX, upper = INT_MIN;
        for (pair<int,int> p: s){
            lower = min(lower, p.first);
            upper = max(upper, p.first);
        }
        int sum = lower + upper;
        for (auto p: s){
            if (s.find(make_pair(sum - p.first, p.second)) == s.end()) return false;
        }
        return true;

    }
};