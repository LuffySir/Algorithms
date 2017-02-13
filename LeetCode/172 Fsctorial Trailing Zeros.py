# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.


def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    # Because all trailing 0 is from factors 5 * 2. But sometimes one number may have several 5 factors,
    # for example, 25 have two 5 factors, 125 have three 5 factors.In the n! operation, factors 2 is always ample.
    # So we just count how many 5 factors in all number from 1 to n.
    return 0 if n == 0 else n / 5 + trailingZeroes(n / 5)


