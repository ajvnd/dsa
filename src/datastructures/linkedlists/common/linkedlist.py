from abc import ABC, abstractmethod
from src.datastructures.linkedlists.common.empty_linkedlist_exception import EmptyLinkedListException


class LinkedList(ABC):
    def __init__(self):
        self.head = None
        self.tail = None

    @abstractmethod
    def add_first(self, value):
        pass

    @abstractmethod
    def add_last(self, value):
        pass

    @abstractmethod
    def add_at(self, index, value):
        pass

    def remove_first(self):
        if self.is_empty():
            raise EmptyLinkedListException()
        self.head = self.head.next

    @abstractmethod
    def remove_last(self):
        pass

    @abstractmethod
    def remove_at(self, index):
        pass

    def peak_first(self):
        if self.is_empty():
            raise EmptyLinkedListException()
        return self.head

    def peak_last(self):
        if self.is_empty():
            raise EmptyLinkedListException()
        return self.tail

    def is_empty(self):
        return self.head is None and self.tail is None

    def _getitem(self, index):
        current_node = self.head
        counter = 0

        while current_node is not None:
            if counter == index:
                return current_node

            current_node = current_node.next
            counter += 1

        raise IndexError()

    def _initialize_linkedlist(self, node):
        self.head = node
        self.tail = self.head

    def _check_index(self, index):
        is_less_then_zero = index < 0
        is_grater_than_len = index > self.__len__()

        if is_less_then_zero or is_grater_than_len:
            raise IndexError("Index out of range")

    def __repr__(self):
        if self.is_empty():
            return "Empty LinkedList"

        current_node = self.head
        value = ""

        while current_node is not None:
            value += " " + self.head
            current_node = current_node.next

        return value

    def __len__(self):
        counter = 0
        current_node = self.head

        while current_node is not None:
            current_node = current_node.next
            counter += 1

        return counter
