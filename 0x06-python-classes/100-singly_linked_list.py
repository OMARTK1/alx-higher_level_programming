#!/usr/bin/python3

class Node:
    """Represent a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.data = data
        self.next_node = next_node

class SinglyLinkedList:
    """Represent a singly linked list."""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return '\n'.join(map(str, result))
