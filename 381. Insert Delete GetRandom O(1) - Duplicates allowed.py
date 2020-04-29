'''
381. Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
Accepted
59,614
Submissions
177,561


'''

# 2020/04/28, too hard, hash table + array

'''
Runtime: 108 ms, faster than 57.44% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 18.4 MB, less than 100.00% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
'''


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        pos = len(self.nums)
        self.nums.append([val, None])
        if val not in self.key_to_index:
            self.key_to_index[val] = [pos]
            self.nums[-1][1] = 0
            return True
        self.key_to_index[val].append(pos)
        self.nums[-1][1] = len(self.key_to_index[val]) - 1
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.key_to_index:
            return False
        # delete the most recent val
        i = self.key_to_index[val].pop()
        if not self.key_to_index[val]: del self.key_to_index[val]
        # get the tail node and the corresponding index in hash
        last, pos = self.nums.pop()
        if last in self.key_to_index and pos < len(self.key_to_index[last]):
            self.key_to_index[last][pos] = i
            self.nums[i] = [last, pos]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)][0]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()