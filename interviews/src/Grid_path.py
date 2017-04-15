# def grid_path(u, r):
#     if u <= 0 or r <= 0:
#         return
#     if u == 1:
#         return r + 1
#     elif r == 1:
#         return u + 1
#     else:
#         return grid_path(u - 1, r) + grid_path(u, r - 1)

# res = grid_path(4,4)
# print(res)

# while 1:
#     s = input()
#     # print(type(s))
#
#     if s != '':
#         n = int(s)
#         sum = 0
#         res = n
#         for i in range(n):
#             sum += i
#             if sum > n:
#                 res = n - 2*(i-2)
#                 break
#         print(res)

def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

# quick_sort([3,5,1,4,9,8,7,5,2],0,8)


nums = int(input().strip())
if nums == 1:
    print(1)
elif nums == 2:
    print(2)
else:
    cars = []
    for i in range(nums):
        car = input().strip().split()
        car = [int(val) for val in car]
        cars.append(car)
    cars = sorted(cars)
    print(cars)
    insect = []
    i = 0
    while i < nums:
        temp = 1
        for j in range(i+1,nums):
            if cars[j][0] <= cars[i][0] + cars[i][1] and cars[i][0] + cars[i][1] <= cars[j][0] + cars[j][1]:
                temp += 1
            else:
                break
        insect.append(temp)
        i += temp
    print(insect)
    insect = sorted(insect,reverse=True)
    res = insect[0]+insect[1]
    print(res)


