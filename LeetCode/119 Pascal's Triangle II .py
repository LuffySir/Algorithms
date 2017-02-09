# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# 39ms
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    pre, beh = [1], [1, 1]
    if rowIndex == 0:
        return pre
    if rowIndex == 1:
        return beh
    for i in range(1, rowIndex):
        pre = beh
        beh = beh + [1]
        for j in range(1, i+1):
            beh[j] = pre[j-1] + pre[j]
    print(beh)
    return beh

getRow(4)

# 36 ms
def getRow1(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row