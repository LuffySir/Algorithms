# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.

# Note:

#     The given integer is guaranteed to fit within the range of a 32-bit signed integer.
#     You could assume no leading zero bit in the integer’s binary representation.


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # bin(5)-->'0b101'
        num_to_bin = bin(num)[2:]
        complement = ''
        for i in num_to_bin:
            if i == '1':
                c = '0'
            elif i == '0':
                c = '1'
            complement += c
        return int(complement, 2)

    # 先找到num的掩码（全为1），然后与num取异或
    def findComplement1(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
