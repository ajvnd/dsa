class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, value):
        if self.head is None:
            self.__initialize_linkedlist(value)
        else:
            node = SinglyLinkedListNode(value)
            node.next = self.head
            self.head = node

    def add_last(self, value):
        if self.head is None:
            self.__initialize_linkedlist(value)
        else:
            self.tail.next = SinglyLinkedListNode(value)
            self.tail = self.tail.next

    def add_at(self, index, value):
        pass

    def __initialize_linkedlist(self, value):
        self.head = SinglyLinkedListNode(value)
        self.tail = self.head

    def __find(self, index):
        counter = 0
        current_node = self.head

        while current_node is not None:

            if counter == index:
                return current_node

            current_node = current_node.next
            counter += 1

        raise IndexError('Index out of range')


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
