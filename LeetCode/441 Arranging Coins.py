# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.

# for 循环导致MemoryError
def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    sums = 0
    for i in range(1, n+1):
        sums += i
        if sums > n:
            print(i-1)
            return i-1
        elif sums == n:
            print(i)
            return i



def arrangeCoins1(n):
    # 韦达定理求解方程（1+x）x/2 = n
    return int((1 + 8 * n) ** 0.5 - 1) / 2

def arrangeCoins2(n):
    start = 1
    end = n
    while start <= end:
        mid = int((start + end) / 2)
        if 0.5*mid*mid + 0.5*mid < n:
            start = mid + 1
        elif 0.5*mid*mid + 0.5*mid > n:
            end = mid - 1
        else:
            print(mid)
            return mid
    print(start -1)
    return start - 1

arrangeCoins2(5)