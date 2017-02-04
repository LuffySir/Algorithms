# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = []
    for i in range(1,numRows+1):
        res.append([1 for j in range(i)])
    for k in range(2, numRows):
        for m in range(1,k):
            res[k][m] = res[k-1][m-1] + res[k-1][m]
    print(res)
    return res

generate(8)

