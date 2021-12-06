from linked_list import Linked_List


def merge_sort(numbers):
    """Sorts numbers in a linked list in ascending order.
    - Divides the linked list into containing a single list, recursively
    - Repeatedly, merge the sublists to produce a sorted linked lists.
    Returns a sorted linked list."""

    if numbers.size() <= 1:
        return numbers
    elif numbers.head is None:
        return numbers

    left_half, right_half = split(numbers)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(numbers):
    """Divides the unsorted linked list into sub linked lists
    """
    if numbers is None or numbers.head == None:
        left_half = numbers
        right_half = None
        return left_half, right_half
    else:
        size = numbers.size()
        mid = size//2

        mid_node = numbers.node_at_index(mid-1)

        left_half = numbers
        right_half = Linked_List()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """Merges two sub linked lists by data in nodes.
    Returns a new, merged list."""

    # Creates a new linked list that contain nodes from
    # merging left right.
    merged = Linked_List()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterates over left and rigth until it reach the tail
    # node of either
    while left_head or right_head:
        # If the head node of left is None, past the tail
        # Adds the node from right to merged linked list.
        if left_head is None:
            current.next_node = right_head
            # Calls next on right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, past the tail
        # Adds the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Calls next on the left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not either tail node
            # obtain node data to peform comparision
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                # Moves left head to the next node
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                # Moves right head to the next node
                right_head = right_head.next_node
        # Moves current to the next node
        current = current.next_node

    # Discards a fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    return merged


l = Linked_List()
l.add(12)
l.add(11)
l.add(10)
l.add(19)
l.add(20)
l.add(8)
l.add(2)
l.add(5)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
