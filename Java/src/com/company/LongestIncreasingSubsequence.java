package com.company;

import java.util.Arrays;

/*
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?



intuition

In this approach, we scan the array from left to right. We also make use of a dp array initialized with all 0's. This dp array is meant to store the increasing subsequence formed by including the currently encountered element. While traversing the nums array, we keep on filling the dp array with the elements encountered so far. For the element corresponding to the j th
  index (nums[j]), we determine its correct position in the dp array(i th
 index) by making use of Binary Search(which can be used since the dp array is storing increasing subsequence) and also insert it at the correct position. An important point to be noted is that for Binary Search, we consider only that portion of the dp array in which we have made the updates by inserting some elements at their correct positions(which remains always sorted). Thus, only the elements upto the i th
  index in the dpdp array can determine the position of the current element in it. Since, the element enters its correct position(i) in an ascending order in the dp array, the subsequence formed so far in it is surely an increasing subsequence. Whenever this position index ii becomes equal to the length of the LIS formed so far(len), it means, we need to update the len as len = len + 1len=len+1.

Note: dp array does not result in longest increasing subsequence, but length of dparray will give you length of LIS.

Consider the example:

input: [0, 8, 4, 12, 2]

dp: [0]

dp: [0, 8]

dp: [0, 4]

dp: [0, 4, 12]

dp: [0 , 2, 12] which is not the longest increasing subsequence, but length of dp array results in length of Longest Increasing Subsequence.


Note: Arrays.binarySearch() method returns index of the search key, if it is contained in the array, else it returns (-(insertion point) - 1). The insertion point is the point at which the key would be inserted into the array: the index of the first element greater than the key, or a.length if all elements in the array are less than the specified key.

Complexity Analysis

Time complexity : O(nlog(n)). Binary search takes log(n)time and it is called n times.

Space complexity : O(n). dp array of size n is used.


 */

public class LongestIncreasingSubsequence {

    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;
        for(int num: nums){
            int i = Arrays.binarySearch(dp, 0, len, num);
            if (i < 0){
                i = -(i + 1);
            }
            dp[i] = num;
            if (i == len){
                len ++;
            }
        }
        return len;
    }

}
