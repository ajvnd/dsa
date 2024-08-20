# TODO: We went wrong that I am not allowed to use type correctly
from __future__ import annotations
from dataclasses import dataclass

from src.datastructures.linkedlists.common.empty_linkedlist_exception import EmptyLinkedListException
from src.datastructures.linkedlists.common.linkedlist import LinkedList


@dataclass
class SinglyLinkedListNode:
    data: any
    next: SinglyLinkedListNode | None = None


class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add_first(self, value):
        new_node = SinglyLinkedListNode(data=value)
        if self.is_empty():
            self._initialize_linkedlist(new_node)
        else:
            node = new_node
            # new node point to head as new head
            node.next = self.head
            # new node become new head
            self.head = node

    def add_last(self, value):
        new_node = SinglyLinkedListNode(value)
        if self.is_empty():
            self._initialize_linkedlist(new_node)
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def add_at(self, index: int, value):
        self._check_index(index)

        new_node = SinglyLinkedListNode(value)

        if self._is_first_item(index):
            self.add_first(value)
        else:
            # find a node before new node
            previous_to_item = self._getitem(index - 1)
            # points to new node
            previous_to_item.next = new_node

            if not self._is_last_item(index):
                # find a node after new node
                next_to_item = self._getitem(index + 1)
                # new node points to the node after it
                new_node.next = next_to_item
            else:
                # new last node becomes new tail, if it does not have anything after.
                self.tail = new_node

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
        self._check_index(index)

        if self.is_empty():
            raise EmptyLinkedListException()

        if self._is_first_item(index):
            self.remove_first()
        elif self._is_last_item(index):
            self.remove_last()
        else:
            previous_to_item = self._getitem(index - 1)
            next_to_item = self._getitem(index + 1)
            previous_to_item.next = next_to_item

