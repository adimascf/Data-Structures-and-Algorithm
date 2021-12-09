def two_sum(list_nums, target=0):

    map = {}
    for idx, n in enumerate(list_nums):
        diff = target - n
        if diff in map:
            return [map[diff]+1, idx+1]
        map[n] = idx
    return [-1]


def three_sum(list_nums, target=0):

    i = 0
    while i < len(list_nums):
        first = -list_nums[i]
        temp = True
        second_third = two_sum(list_nums[i+1:], first)
        if second_third == [-1]:
            temp = False
        if temp:
            return [i+1] + list(map(lambda x: x+i+1, second_third))
        i += 1

    return [-1]


print(three_sum([8, -6, 4, -2, -8]))


# with open('E:algorithm_datatest/rosalind_3sum.txt', 'r') as f:
#     f.readline()
#     content = f.readlines()
#     nums_test = []
#     for item in content:
#         item = item.strip().split(' ')
#         temp = list(map(lambda x: int(x), item))
#         nums_test.append(temp)
# print(len(nums_test))
# for nums in nums_test:
#     print(*three_sum(nums))
