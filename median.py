def median(numbers, k):
    """Find the k-th smallest element in the list of number.
    Input parameters are a list of unsorted numbers and integer k.
    Returns integer."""
    pivot = numbers[0]
    less_than = []
    greater_than = []
    for num in numbers[1:]:
        if num <= pivot:
            less_than.append(num)
        else:
            greater_than.append(num)

    length_left = len(less_than)
    if length_left == k - 1:
        return pivot
    elif length_left > k - 1:
        return median(less_than, k)
    else:
        return median(greater_than + [pivot], k - length_left)


with open('E:algorithm_datatest/rosalind_med.txt', 'r') as f:
    f.readline()
    test_arr = f.readline().strip().split(' ')
    test_arr = list(map(lambda x: int(x), test_arr))
    k_test = int(f.readline().strip())
print(median(test_arr, k_test))
