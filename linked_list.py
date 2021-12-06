from typing import Counter


class Node:
    """An object to store a single node of linked list.
    Two attributes, data and the link of the next node"""
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f'<Node data: {self.data}>'


class Linked_List:
    """Singly linked list
    """

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        length = 0

        while current != None:
            length += 1
            current = current.next_node
        return length

    def add(self, data):
        """Add new node containing data at the head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """Search for the first node containing data that match the key.
        Return None if key doesn't found
        """
        current = self.head
        while current != None:
            if current.data == key:
                return current
            current = current.next_node
        return None

    def insert(self, data, index):
        """Insert a new node containing data at a given position
        Insertion takes O(1) time, but finding the element takes O(n).
        Overall linear time."""

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next = current.next_node

            prev.next_node = new
            new.next_node = next

    def remove(self, key):
        """Removes node containinng data that mathces the key"""
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found == True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self) -> str:
        """Return string representation cointaining the linked list
        it takes O(n)"""
        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return ' -> '.join(nodes)
