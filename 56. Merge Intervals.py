"""
56. Merge Intervals


Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=operator.attrgetter('start'))
        res = []
        for itv in intervals:
            if not res:
                res.append(itv)
                tmp = itv
                continue
            if itv.start <= tmp.end:
                if itv.end > tmp.end:
                    res.pop()
                    tmp = Interval(tmp.start, itv.end)
                    res.append(tmp)
            else:
                res.append(itv)
                tmp = itv
        return res

# c++, rewrite

'''
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if (intervals.empty()) return intervals;
        sort(intervals.begin(), intervals.end(), [](Interval& a, Interval& b){ return a.start < b.start; });
        vector<Interval> res;
        int l = intervals[0].start, r = intervals[0].end;
        for (int i = 1; i < intervals.size(); ++i){
            if (intervals[i].start > r){
                res.push_back(Interval(l, r));
                l = intervals[i].start; r = intervals[i].end;
            }
            else{
                r = max(r, intervals[i].end);
            }
            
        }
        res.push_back(Interval(l, r));
        return res;
        
    }
    
};

'''




