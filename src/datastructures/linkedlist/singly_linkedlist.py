class EmptyLinkedListException(Exception):
    def __init__(self, message="The linked list is empty."):
        self.message = message
        super().__init__(self.message)


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, value):
        if self.is_empty():
            self.__initialize_linkedlist(value)
        else:
            node = SinglyLinkedListNode(value)
            node.next = self.head
            self.head = node

    def add_last(self, value):
        if self.is_empty():
            self.__initialize_linkedlist(value)
        else:
            self.tail.next = SinglyLinkedListNode(value)
            self.tail = self.tail.next

    def add_at(self, index, value):
        pass

    def remove_first(self):
        if self.is_empty():
            raise EmptyLinkedListException()
        self.head = self.head.next

    def remove_last(self):
        if self.is_empty():
            raise EmptyLinkedListException()

    def remove_at(self, index):
        if self.is_empty():
            raise EmptyLinkedListException()
    def is_empty(self):
        return self.head is None and self.tail is None

    def peak_first(self):
        if self.is_empty():
            raise EmptyLinkedListException()
        return self.head.data

    def peak_last(self):
        if self.is_empty():
            raise EmptyLinkedListException()
        return self.tail.data

    def __initialize_linkedlist(self, value):
        self.head = SinglyLinkedListNode(value)
        self.tail = self.head

    def __len__(self):
        counter = 0
        current_node = self.head

        while current_node is not None:
            current_node = current_node.next
            counter += 1

        return counter
