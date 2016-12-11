# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


# public int getSum(int a, int b) {
#  if(b == 0){//没有进为的时候完成运算
#     return a;
# }
# int sum,carry;
# sum = a^b;//完成第一步加发的运算
# carry = (a&b)<<1;//完成第二步进位并且左移运算
# return getSum(sum,carry);//
# }

# 求和
# // Iterative
# public int getSum(int a, int b) {
#     if (a == 0) return b;
#     if (b == 0) return a;

#     while (b != 0) {
#         int carry = a & b;
#         a = a ^ b;
#         b = carry << 1;
#     }

#     return a;
# }

# 差
# // Iterative
# public int getSubtract(int a, int b) {
#     while (b != 0) {
#         int borrow = (~a) & b;
#         a = a ^ b;
#         b = borrow << 1;
#     }

#     return a;
# }

# // Recursive
# public int getSum(int a, int b) {
#     return (b == 0) ? a : getSum(a ^ b, (a & b) << 1);
# }

# // Recursive
# public int getSubtract(int a, int b) {
#     return (b == 0) ? a : getSubtract(a ^ b, (~a & b) << 1);
# }

# 相反数
# // Get negative number
# public int negate(int x) {
#     return ~x + 1;
# }
