from src.datastructures.arrays.staticArray import StaticArray


class DynamicArray(StaticArray):
    def __init__(self, item_type):
        super().__init__(item_type, 2)

    def append(self, item):
        if super().__len__() + 1 >= self._capacity:
            self._capacity *= 2
            self._container += ([None] * (self._capacity - super().__len__() - 1))

        super().__setitem__(super().__len__(), item)

    def insert(self, index, item):

        for i in range(index, self._capacity):
            self._container[i + 1] = self._container[i]

        super().__setitem__(index, item)

    def __delitem__(self, index):
        super().__delitem__(index)

        if index + 1 >= self._capacity:
            return

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
    del da[2]
    da.insert(1, 21)

    print(da)
