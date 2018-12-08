"""
253. Meeting Rooms II


Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1


"""

'''

Algorithm

Sort the given meetings by their start time.
Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
If not, then we allocate a new room and add it to the heap.
After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals. sort(key = lambda elem: elem.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i].end)
        return len(rooms)

# c++

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
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), cmp);
        priority_queue<int, vector<int>, greater<int> > rooms;
        for (auto time: intervals){
            if(!rooms.empty() && rooms.top() <= time.start) rooms.pop();
            rooms.push(time.end);
        }
        return rooms.size();
        
    }
    
    static bool cmp(Interval &a , Interval &b){
        return a.start < b.start;
    }
};

'''