from common.empty_linkedlist_exception import EmptyLinkedListException
from common.linkedlist import LinkedList


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add_first(self, value):
        if self.is_empty():
            self._initialize_linkedlist(SinglyLinkedListNode(value))
        else:
            node = SinglyLinkedListNode(value)
            node.next = self.head
            self.head = node

    def add_last(self, value):
        if self.is_empty():
            self._initialize_linkedlist(SinglyLinkedListNode(value))
        else:
            self.tail.next = SinglyLinkedListNode(value)
            self.tail = self.tail.next

    def add_at(self, index, value):
        pass

    def remove_last(self):
        if self.is_empty():
            raise EmptyLinkedListException()

        if self.head == self.tail:
            self.head = None
            self.tail = None

        previous_to_tail = self._getitem(self.__len__() - 2)
        previous_to_tail.next = None
        self.tail = previous_to_tail

    def remove_at(self, index):
        if self.is_empty():
            raise EmptyLinkedListException()
