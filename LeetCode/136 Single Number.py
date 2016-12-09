# Given an array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for key, val in dic.items():
        if val == 1:
            return key


def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
# ^：异或（按位，值不同时为1），交换顺序不影响结果，如
# => 0 ^ 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1
# => 0^ 2^2 ^ 1^1 ^ 4^4 ^5 (Rearranging, taking same numbers together)
# => 0 ^ 0 ^ 0 ^ 0 ^ 5
# => 0 ^ 5
# => 5


def singleNumber3(self, nums):
    return 2 * sum(set(nums)) - sum(nums)


def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)


def singleNumber(self, nums):
    return reduce(operator.xor, nums)


