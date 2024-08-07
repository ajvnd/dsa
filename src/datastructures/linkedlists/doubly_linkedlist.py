from src.datastructures.linkedlists.common.linkedlist import LinkedList


class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add_first(self, value):
        pass

    def add_last(self, value):
        pass

    def add_at(self, index, value):
        pass

    def remove_last(self):
        pass

    def remove_at(self, index):
        pass
