/*
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).



Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.


Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:
*/

class Solution {
public:
    bool isConvex(vector<vector<int>>& points) {
        long prev = det(points[0], points[1], points[2]);
//        cout << points[1][0] << " " << points[1][1] << endl;
        for (int i = 1; i <= points.size(); ++i){
            long curr = det(points[i % points.size()], points[(i + 1) % points.size()], points[(i + 2) % points.size()]);
//            cout << prev << " "<< curr << endl;
            if (curr * prev < 0) return false;
            else if (prev == 0 && curr != 0) prev = curr;
        }
        return true;

    }

    long det(vector<int> &p0, vector<int> & p1, vector<int> & p2){
        vector<int> e1{p1[0] - p0[0], p1[1] - p0[1]}, e2{p2[0] - p0[0], p2[1] - p0[1]};
        return e1[0] * e2[1] - e1[1] * e2[0];
    }
};