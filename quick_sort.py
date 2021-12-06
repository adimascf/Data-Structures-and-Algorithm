def quicksort(values):
    """Recursively, get the first value as pivot in the list of number
    Divide into two sublist less than pivot and greater than pivot
    concacenate less than pivot sublist, pivot, and greater than sub list"""
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for num in values[1:]:
        if num <= pivot:
            less_than_pivot.append(num)
        else:
            greater_than_pivot.append(num)
    # print('%15s %1s %15s' % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


with open('E:algorithm_datatest/rosalind_qs.txt', 'r') as f:
    f.readline()
    test_case = f.read().strip().split(' ')
    test_case = list(map(lambda x: int(x), test_case))
    print(*quicksort(test_case))
