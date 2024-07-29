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
        new_node = SinglyLinkedListNode(value)
        if self.is_empty():
            self._initialize_linkedlist(new_node)
        else:
            node = new_node
            node.next = self.head
            self.head = node

    def add_last(self, value):
        new_node = SinglyLinkedListNode(value)
        if self.is_empty():
            self._initialize_linkedlist(new_node)
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def add_at(self, index, value):
        new_node = SinglyLinkedListNode(value)

        if self.is_empty():
            self._initialize_linkedlist(new_node)
        elif self.__is_first_item(index):
            self.add_first(value)
        elif self.__is_last_item(index):
            self.add_last(value)
        else:
            previous_to_item = self._getitem(index - 1)
            next_to_item = self._getitem(index + 1)
            previous_to_item.next = new_node
            new_node.next = next_to_item

    def remove_last(self):
        if self.is_empty():
            raise EmptyLinkedListException()

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            previous_to_tail = self._getitem(self.__len__() - 2)
            previous_to_tail.next = None
            self.tail = previous_to_tail

    def remove_at(self, index):
        if self.is_empty():
            raise EmptyLinkedListException()

        if self.__is_first_item(index):
            self.remove_first()
        elif self.__is_last_item(index):
            self.remove_last()
        else:
            previous_to_item = self._getitem(index - 1)
            next_to_item = self._getitem(index + 1)
            previous_to_item.next = next_to_item

    def __is_first_item(self, index):
        return index == 0

    def __is_last_item(self, index):
        return index == self.__len__() - 1
