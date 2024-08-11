from src.datastructures.linkedlists.singly_linkedlist import SinglyLinkedList


class Stack:

    def __init__(self):
        self.item = SinglyLinkedList()

    def is_empty(self):
        return self.item.is_empty()

    def push(self, item):
        self.item.add_first(item)
        pass

    def pop(self):
        item = self.item.peak_first()
        self.item.remove_first()
        return item.value

    def peek(self):
        item = self.item.peak_first()
        return item.value

    def size(self):
        self.item.remove_first()
        pass
