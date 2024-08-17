from src.datastructures.arrays.static_array import StaticArray


# The below code inherits many of its functionality from static_array


class DynamicArray(StaticArray):
    def __init__(self, item_type):
        super().__init__(item_type, 1)

    def append(self, item):
        # if the number of items reached capacity, then double the size of array
        if self.__is_reached_the_capacity():
            self.__double_capacity()

        super().__setitem__(super().__len__(), item)

    def insert(self, index: int, item):
        # if the number of items reached capacity, then double the size of array
        if self.__is_reached_the_capacity():
            self.__double_capacity()

        # shifting items to the right from last item to current item in index
        for i in range(self.__len__(), index, -1):
            self._container[i] = self._container[i - 1]

        # set new value after shifting items
        super().__setitem__(index, item)

    def remove(self, item):
        index = super().get_index(item)
        self.__delitem__(index)

    def __is_reached_the_capacity(self):
        return super().__len__() == self._capacity

    def __double_capacity(self):
        self._capacity *= 2
        self._container += ([None] * (self._capacity - super().__len__()))

    def __delitem__(self, index):
        super().__delitem__(index)

        is_index_of_last_item = index + 1 >= self._capacity

        if is_index_of_last_item:
            return  # just delete it and there is no need for shifting

        # Shift all right items to the left
        for i in range(index, self._capacity):
            if i + 1 >= self._capacity:
                break

            self._container[i] = self._container[i + 1]

