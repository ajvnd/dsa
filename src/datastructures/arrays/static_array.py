class StaticArray():
    def __init__(self, item_type, capacity):

        # make sure the capacity is greater or equal to zero
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self._capacity = capacity
        self._container = [None] * capacity

        # make sure the data type of items is a primitive data type
        if item_type not in [int, float, str, bool]:
            raise TypeError("Item type must be a primitive data type")

        self.__item_type = item_type

    def __getitem__(self, index):
        self.__check_index(index)
        return self._container[index]

    def __setitem__(self, index, value):
        self.__check_index(index)

        # Check if the provided value matches the expected type for elements in the array.
        if not isinstance(value, self.__item_type):
            raise TypeError(f"Expected item of type {self.__item_type.__name__}, but got {type(value).__name__}")

        self._container[index] = value

    def __delitem__(self, index):
        self.__check_index(index)
        self._container[index] = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self._container})"

    def __iter__(self):
        return iter(self._container)

    def __len__(self):
        return sum(1 for x in self._container if x is not None)

    def get_index(self, value):
        for index, item in enumerate(self._container):
            if item is not None and item == value:
                return index

    def reverse(self):
        # filter out none items
        items = [i for i in self._container if i is not None]
        # reverse remains
        items = items[::-1]
        # calculate number of none items required to be attached to new reversed list
        remains = self._capacity - len(items)
        # make the reverse array with proper number of none items
        self._container = items + [None] * remains

    def sort(self):
        pass  # TODO: Once I implement this feature in the future, I pass it to this function

    def binary_search(self):
        pass  # TODO: Once I implement this feature in the future, I pass it to this function

    def __check_index(self, index):
        is_integer = isinstance(index, int)
        is_less_then_zero = index < 0
        is_grater_equal_to_capacity = index >= self._capacity

        # Check if the index is integer  value matches the expected type for elements in the array.
        if not is_integer or is_less_then_zero or is_grater_equal_to_capacity:
            raise IndexError("Index out of range")


if __name__ == '__main__':

    array = StaticArray(str, 5)

    array[0] = "A"
    array[1] = "B"
    array[2] = "C"

    array.reverse()
    print(array)
