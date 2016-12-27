#  A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the
# bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]

    def readBinaryWatch1(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        ans = []
        for i in range(0, num + 1):
            for _h in self.get_time(hours, i, 12):
                for _m in self.get_time(minutes, num - i, 60):
                    ans.append('{:}:{:02}'.format(_h, _m))
        return ans

    def get_time(self, time, n, limit):
        ans = []
        # itertools.combinations 排列组合
        for comb in itertools.combinations(time, n):
            tmp = sum(comb)
            if tmp < limit:
                ans.append(tmp)
        return ans
