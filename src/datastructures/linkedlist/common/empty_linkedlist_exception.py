class EmptyLinkedListException(Exception):
    def __init__(self, message="The linked list is empty."):
        self.message = message
        super().__init__(self.message)