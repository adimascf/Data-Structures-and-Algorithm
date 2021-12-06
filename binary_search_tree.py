class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_traversal(tree.root, "")[:-1]
        elif traversal_type == 'inorder':
            return self.inorder_traversal(tree.root, "")[:-1]
        elif traversal_type == 'postorder':
            return self.postorder_traversal(tree.root, "")[:-1]
        elif traversal_type == 'levelorder':
            return self.levelorder_traversal(tree.root)[:-1]
        elif traversal_type == 'reverse level order':
            return self.reverse_level_order_traversal(tree.root)[:-1]
        else:
            return f"Traversal type {traversal_type} is not suported"

    def preorder_traversal(self, start, traversal):
        """Visit -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        """Left -> Visit -> Right"""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """Left -> Right -> Visit"""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_traversal(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_level_order_traversal(self, start):

        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ''
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + '-'
        return traversal


tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree('reverse level order'))
