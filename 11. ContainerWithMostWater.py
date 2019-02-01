'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''

'''

Time limit exceeded

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nb=len(height)
        area=-1
        for i in range(nb):
            for j in range(i+1,nb):
                tmp=min(height[i],height[j])*(j-i)
                if tmp>area:
                    area=tmp
        return area
        


'''

#two pointers, not my idea

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nb=len(height)
        area=-1
        l=0
        r=nb-1
        while l<r:
            area=max(area,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area

'''
// cpp 

class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = INT_MIN, l = 0, r = height.size() - 1;
        while (l < r){
            area = max(area, (r - l) * min(height[l], height[r]));
            if (height[l] < height[r]) ++l;
            else --r;
        }
        return area;
        
    }
};
'''