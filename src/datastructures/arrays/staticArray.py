class StaticArray():
    def __init__(self, capacity, item_type):

        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self._capacity = capacity
        self._container = [None] * capacity

        if item_type not in [int, float, str, bool]:
            raise ValueError("Item type must be a primitive data type")

        self.__item_type = item_type

    def __getitem__(self, index):
        self.__check_index(index)
        return self._container[index]

    def __setitem__(self, index, value):
        self.__check_index(index)

        if not isinstance(value, self.__item_type):
            raise TypeError(f"Expected item of type {self.__item_type.__name__}, but got {type(value).__name__}")

        self._container[index] = value

    def __delitem__(self, index):
        self.__check_index(index)
        self._container[index] = None

    def __repr__(self):
        return f"StaticArray({[x for x in self._container if x is not None]})"

    def __iter__(self):
        return iter(self._container)

    def __len__(self):
        return sum(1 for x in self._container if x is not None)

    def __check_index(self, index):
        if not isinstance(index, int) or index < 0 or index >= self._capacity:
            raise IndexError("Index out of range")


if __name__ == '__main__':

    array = StaticArray(5, str)

    array[0] = "A"
    array[1] = "B"
    array[2] = "C"
    array[3] = "D"
    array[4] = "E"

    for i in array:
        print(i)
