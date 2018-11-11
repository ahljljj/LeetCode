"""

401. Binary Watch


A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".



"""


# dfs : ridiculous slow


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        res = []
        for m in range(0, min(num + 1, 5)):
            self.hours = set()
            self.gethours(hours, 0, m, 0)
            n = num - m if num - m > 0 else 0
            self.minutes = set()
            self.getminutes(minutes, 0, n, 0)
            res.extend([h + ":" + m for h in self.hours for m in self.minutes])

        return res

    def gethours(self, hours, time, num, idx):
        if time > 11 or num < 0:
            return
        if num == 0:
            self.hours.add(str(time))
            return
        for i in range(idx, len(hours)):
            self.gethours(hours, hours[i] + time, num - 1, i + 1)
        return

    def getminutes(self, minutes, time, num, idx):
        if time > 59 or num < 0:
            return
        if num == 0:
            if time < 10:
                time = "0" + str(time)
            self.minutes.add(str(time))
            return
        for i in range(idx, len(minutes)):
            self.getminutes(minutes, minutes[i] + time, num - 1, i + 1)
        return



