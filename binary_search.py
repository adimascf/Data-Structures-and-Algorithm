
def binary_search(numbers, num_target):
    """Using binary search algorithm, find index position
    of number target in number. returns index integer if it is found,
    otherwise returns None"""
    start = 0
    end = len(numbers)-1
    while start <= end:
        mid = (start + end)//2
        # print(start, mid, end)
        if numbers[mid] == num_target:
            return mid
        elif numbers[mid] < num_target:
            start = mid + 1
        else:
            end = mid - 1
    # print(start, mid, end)
    return None


numbers_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target_test = 111
print(binary_search(numbers_test, target_test))
