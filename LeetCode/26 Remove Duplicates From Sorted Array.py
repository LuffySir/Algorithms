#  Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

# 最后一个用例超时
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pre, beh, k = 0, 1, len(nums)
    while beh < k:
        if nums[pre] == nums[beh]:
            nums.remove(nums[pre])
            k -= 1
        else:
            pre, beh = beh, beh + 1
    print(nums)
    return len(nums)

removeDuplicates([1,2])


def removeDuplicates1(A):
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]

    return newTail + 1