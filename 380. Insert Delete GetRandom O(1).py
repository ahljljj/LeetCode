"""
380. Insert Delete GetRandom O(1)


Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();



"""



#  The main trick is when you remove a value. ArrayList's remove method is O(n) if you remove from random location. To overcome that, we swap the values between (randomIndex, lastIndex) and always remove the entry from the end of the list. After the swap, you need to update the new index of the swapped value (which was previously at the end of the list) in the map.


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.res:
            self.nums.append(val)
            self.res[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.res:
            idx, last = self.res[val], self.nums[-1]
            self.nums[idx], self.res[last] = last, idx
            self.nums.pop()
            self.res.pop(val, None)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



# dictionary + dictionary

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = {}
        self.nums = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.res:
            idx = len(self.res)
            self.nums[idx] = val
            self.res[val] = idx
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.res:
            idx = self.res[val]
            last = self.nums[len(self.nums) - 1]
            self.nums[idx] = last
            self.res[last] = idx
            self.res.pop(val, None)
            self.nums.pop(len(self.nums) - 1, None)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# 2020/04/28, too hard, hashtable + array

'''
Runtime: 96 ms, faster than 89.94% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 18 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).
'''


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.key_to_index:
            return False
        self.nums.append(val)
        self.key_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.key_to_index:
            return False
        i = self.key_to_index[val]
        tail = self.nums.pop()
        if i < len(self.nums):
            self.nums[i] = tail
            self.key_to_index[tail] = i
        del self.key_to_index[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()