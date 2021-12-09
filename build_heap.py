def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def heapify(arr, n, i):

    left = left_child(i)
    right = right_child(i)

    if left < n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr, n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr, n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


with open('E:algorithm_datatest/rosalind_hea.txt', 'r') as f:
    n_test = int(f.readline())
    arr_test = f.read().strip().split(' ')
    arr_test = list(map(lambda x: int(x), arr_test))

# # n_test = 9
# arr_test = [2, 6, 7, 1, 3, 5, 4, 8, 9]
build_max_heap(arr_test, n_test)
print(*arr_test)
