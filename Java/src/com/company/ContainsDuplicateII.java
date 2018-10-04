package com.company;

import java.util.TreeSet;

public class ContainsDuplicateII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {

        if (nums == null || nums.length == 0 || k <=0 || t < 0){
            return false;
        }

        TreeSet<Integer> set = new TreeSet();
        for (int i = 0; i < nums.length; i++){
            // the smallest number larger than nums[i]
            Integer ceil = set.ceiling(nums[i]);
            if (ceil != null && Long.valueOf(ceil) - Long.valueOf(nums[i]) <= t){
                return true;
            }
            // the larget number smaller than nums[i]
            Integer floor = set.floor(nums[i]);
            if (floor != null && Long.valueOf(nums[i]) - Long.valueOf(floor) <=t){
                return true;
            }
            set.add(nums[i]);
            if (i >= k){
                set.remove(nums[i-k]);
            }
        }
        return false;
    }
}
