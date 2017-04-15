# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
# so the function should return 3.


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    # res = bin(n).count('1')
    # print(res)
    res = 0
    while(n):
        res += 1
        n = n & (n-1)
    print(res)
    return res

hammingWeight(15)
