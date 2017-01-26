# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up
# to the target, where index1 must be less than index2. Please note that your returned
# answers (both index1 and index2) are not zero-based.


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start = 0
    end = len(numbers) - 1
    while numbers[start] + numbers[end] != target:
        if numbers[start] + numbers[end] < target:
            start += 1
        else:
            end -= 1
    print([start+1,end+1])
    return [start+1,end+1]

twoSum([2,7,11,15],9)


