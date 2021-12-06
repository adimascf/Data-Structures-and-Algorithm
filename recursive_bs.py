def recursive_binary_search(numbers, start, end, target):
    """Using binary search algorithm, recursively find index position
    of number target in number. returns index integer if it is found,
    otherwise returns None"""
    mid = (start + end)//2
    if start <= end:
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            return recursive_binary_search(numbers, start, mid-1, target)
        else:
            return recursive_binary_search(numbers, mid+1, end, target)
    else:
        return None


def recursive_binary_search_2(numbers, target):
    """Using binary search algorithm, recursively find index position
    of number target in number. returns True if it is found,
    otherwise returns False"""
    # print(numbers)
    if len(numbers) == 0:
        return False
    else:
        mid = len(numbers)//2
        if numbers[mid] == target:
            return True
        elif numbers[mid] > target:
            return recursive_binary_search_2(numbers[:mid], target)
        else:
            return recursive_binary_search_2(numbers[mid+1:], target)


numbers_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target_test = 1
print(recursive_binary_search(numbers_test, 0, len(numbers_test)-1, target_test))
print(recursive_binary_search_2(numbers_test, target_test))
