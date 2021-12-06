def two_way_partition(numbers):
    """Gets the pivot, which is number in the first index of the list.
    Divides a list of numbers into sublist less than the pivot and
    greater than the pivot.
    returns concacenated less than pivot sublist + sublist + greater than pivot sublist"""

    pivot = numbers[0]
    less_than_pivot = []
    greater_than_pivot = []
    for num in numbers[1:]:
        if num <= pivot:
            less_than_pivot.append(num)
        else:
            greater_than_pivot.append(num)
    return less_than_pivot + [pivot] + greater_than_pivot


def three_way_partition(numbers):
    """Get the number in the first indext of the numbers list as pivot.
    Divides numbers list input into three sublists, less than, equal than, and greater than pivot.
    Returns concacenated those sublist into a single list again."""
    pivot = numbers[0]
    less_than = []
    equal = []
    greater_than = []
    for num in numbers[1:]:
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            less_than.append(num)
        else:
            greater_than.append(num)
    return less_than + [pivot] + equal + greater_than


with open('E:algorithm_datatest/rosalind_par3.txt', 'r') as f:
    f.readline()
    test_case = f.read().strip().split(' ')
    test_case = list(map(lambda x: int(x), test_case))
print(*three_way_partition(test_case))
