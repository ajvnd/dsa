# TODO: We went wrong that I am not allowed to use type correctly
from __future__ import annotations
from dataclasses import dataclass

from src.datastructures.linkedlists.common.linkedlist import LinkedList


@dataclass
class DoublyLinkedListNode:
    data: any
    next: DoublyLinkedListNode | None = None
    prev: DoublyLinkedListNode | None = None


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add_first(self, value):
        new_node = DoublyLinkedListNode(data=value)
        if self.is_empty():
            self._initialize_linkedlist(new_node)
        else:
            node = new_node
            # new node point to head as new head
            node.next = self.head
            # old head point back to new node
            self.head.prev = node
            # new node become new head
            self.head = node

    def add_last(self, value):
        new_node = DoublyLinkedListNode(value)
        
        if self.is_empty():
            self._initialize_linkedlist(new_node)
        else:
            # link the current tail's next to the new node
            self.tail.next = new_node
            # update the tail reference to the new node
            self.tail = self.tail.next

    def add_at(self, index, value):
        pass

    def remove_last(self):
        pass

    def remove_at(self, index):
        pass
