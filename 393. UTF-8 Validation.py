"""
393. UTF-8 Validation



The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.



"""

# greedy?
# time complexity O(8 * n)


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = len(data)
        i = 0
        while i < n:
            len_bytes = self.countbytes(data[i])
            if len_bytes == 1 or len_bytes > 4: # length has to less than 5
                return False
            if len_bytes == 0:
                len_bytes += 1
            for j in range(i + 1, i + len_bytes):
                if j >= n:
                    return False
                top = data[j] >> 6 # return the top 2 significant digits
                if top != 2:
                    return False
            i += len_bytes

        return True

    def countbytes(self, num): # compute the length of the bytes
        count = 0
        for i in range(8):
            last = num & 1
            if last == 1:
                count += 1
            else:
                count = 0
            num >>= 1
        return count


# finite number of choices here: we can use if-else to list all possibilities

class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for num in data:
            if count == 0:
                if num >> 3 == 0b11111:
                    return False
                elif num >> 4 == 0b1111:
                    count = 4 - 1
                elif num >> 5 == 0b111:
                    count = 3 - 1
                elif num >> 6 == 0b11:
                    count = 2 - 1
                elif num >> 7 == 0b1:
                    return False
                else:
                    count = 1 - 1
            else:
                if num >> 6 != 0b10:
                    return False
                else:
                    count -= 1
        return True if not count else False
