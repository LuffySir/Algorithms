#  Given an integer, write an algorithm to convert it to hexadecimal.
# For negative integer, two’s complement method is used.

# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented
# by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly


class Solution(object):
    def toHex(self, num):
        if num == 0:
            return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15       # this means num & 1111b
            c = mp[n]          # get the hex char
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  # strip leading zeroes

    def toHex1(self, num):
        ans = []
        dic = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        if num == 0:
            return "0"
        if num < 0:
            num = num + 2**32

        while num > 0:
            digit = num % 16
            num = (num - digit) / 16
            if digit > 9 and digit < 16:
                digit = dic[digit]
            else:
                digit = str(digit)
            ans.append(digit)
        return "".join(ans[::-1])
