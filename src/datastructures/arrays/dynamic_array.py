from src.datastructures.arrays.static_array import StaticArray


class DynamicArray(StaticArray):
    def __init__(self, item_type):
        super().__init__(item_type, 2)

    def append(self, item):
        is_array_reached_capacity = super().__len__() + 1 >= self._capacity

        # if the number of items reached capacity, then double the size of array
        if is_array_reached_capacity:
            self._capacity *= 2
            self._container += ([None] * (self._capacity - super().__len__() - 1))

        super().__setitem__(super().__len__(), item)

    def insert(self, index, item):

        # TODO: I am still thinking of finding the an element and efficient way.
        for i in range(index, self._capacity):
            self._container[i + 1] = self._container[i]

        super().__setitem__(index, item)

    def remove(self, item):
        index = super().get_index(item)
        self.__delitem__(index)

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


if __name__ == '__main__':
    da = DynamicArray(int)
    da.append(1)
    da.append(2)
    da.append(3)
    da.append(4)
    da.remove(4)
    print(da)
