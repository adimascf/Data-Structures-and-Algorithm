import sys
sys.setrecursionlimit(10000)


def split(values):
    """
    Divides the unsorted list at midpoin into sublists
    Returns two sublists (left and right)"""
    mid = len(values)//2
    left_half = values[:mid]
    right_half = values[mid:]
    return left_half, right_half


def merge(left_half, right_half):
    """
    Merges two lists, sorting them in the process.
    Returns a new merged list"""
    l = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            l.append(left_half[i])
            i += 1
        else:
            l.append(right_half[j])
            j += 1

    while i < len(left_half):
        l.append(left_half[i])
        i += 1
    while j < len(right_half):
        l.append(right_half[j])
        j += 1

    return l


def merge_sort(values):
    """
    Sorts a list in ascending order
    returns a new sorted list
    Divide: Find the midpoin of the list and divide into the sublist
    Conquer: Recursively sort the sublists created in previous step
    Combine : Merge sorted sublists created in the previous step.
    Takes O(n log n) time.
    """
    if len(values) <= 1:
        return values

    left_half, right_half = split(values)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def verivy_sorted(the_lists):
    n = len(the_lists)
    if n <= 1:
        return True
    else:
        return the_lists[0] <= the_lists[1] and verivy_sorted(the_lists[1:])


with open("E:algorithm_datatest/rosalind_ms.txt", "r") as f:
    f.readline()
    test_case = f.read().strip().split(' ')
test_case = list(map(lambda x: int(x), test_case))
l = merge_sort(test_case)
print(*l)
