from src.datastructures.linkedlists.singly_linkedlist import SinglyLinkedList
from src.datastructures.stacks.empty_stack_exception import EmptyStackException


class Stack:

    def __init__(self):
        self.list = SinglyLinkedList()

    def is_empty(self):
        return self.list.is_empty()

    def push(self, item):
        self.list.add_first(item)
        pass

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()

        item = self.list.peak_first()
        self.list.remove_first()
        return item.value

    def peek(self):
        if self.is_empty():
            raise EmptyStackException()

        item = self.list.peak_first()
        return item.value

    def size(self):
        self.list.remove_first()
        pass
