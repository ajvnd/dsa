import pytest

from src.datastructures.arrays.static_array import StaticArray


class TestStaticArray:

    @pytest.fixture
    def static_array(self):
        return StaticArray(int, 5)

    def test_init_initialize_fields(self, static_array):
        # arrange

        # act

        # assert
        assert isinstance(static_array, StaticArray)
        assert static_array._capacity == 5
        assert static_array.__dict__['_StaticArray__item_type'] == int

    def test_init_raises_exception_for_negative_capacity(self, static_array):
        # arrange
        data_type = None
        capacity = -1

        # act and assert
        with pytest.raises(ValueError):
            StaticArray(data_type, capacity)

    def test_init_raises_exception_for_non_primitive_type(self, static_array):
        # arrange
        data_type = None
        capacity = 5

        # act and assert
        with pytest.raises(TypeError):
            StaticArray(data_type, capacity)

    def test_init_raises_exception_for_inconsistent_type(self, static_array):
        # arrange
        new_item = 'five'

        # act and assert
        with pytest.raises(TypeError):
            static_array[0] = new_item

    def test_getitem_retrieves_items(self, static_array):
        # arrange
        new_item = 5

        # act
        static_array[0] = new_item

        # assert
        assert static_array[0] == new_item

    def test_setitem_raises_exception_for_invalid_index(self, static_array):
        # arrange
        new_item = 5

        # act & assert
        with pytest.raises(IndexError):
            static_array[6] = new_item

    @pytest.mark.parametrize("index", [(0), (1), (2), (3), (4)])
    def test_setitem_stores_items(self, index, static_array):
        # arrange
        new_item = 5

        # act
        static_array[index] = new_item

        # assert
        assert static_array[index] == new_item

    def test_delitem_removes_items(self, static_array):
        # arrange
        static_array[0] = 5

        # act
        del static_array[0]

        # assert
        assert static_array[0] is None

    def test_repr_represent_items(self, static_array):
        # arrange
        static_array[0] = 5
        static_array[1] = 6
        # act
        items = str(static_array)

        # assert
        assert isinstance(items, str)
        assert "StaticArray([5, 6, None, None, None])" == str(static_array)

    def test_iter_iterates_over_items(self, static_array):
        # act and assert
        for item in static_array:
            assert item is None

    def test_len_returns_length(self, static_array):
        # arrange
        new_item = 5

        # act
        static_array[0] = new_item

        # assert
        assert len(static_array) == 1

    def test_get_index_returns_index(self, static_array):
        # arrange
        static_array[0] = 5

        # act
        index = static_array.get_index(5)

        # assert
        assert index == 0

    def test_reverse_reverses_items(self, static_array):
        # arrange
        static_array[0] = 5
        static_array[1] = 6
        static_array[2] = 7
        static_array[3] = 8

        # act
        static_array.reverse()

        # assert
        assert static_array[0] == 8
        assert static_array[1] == 7
        assert static_array[2] == 6
        assert static_array[3] == 5
        assert static_array[4] is None

    @pytest.mark.xfail(reason="This functionality has not implemented")
    def test_sort_sorts_items_correctly(self, static_array):
        raise NotImplemented("This functionality has not implemented")

    @pytest.mark.xfail(reason="This functionality has not implemented")
    def test_binary_search_performs_binary_search_correctly(self, static_array):
        raise NotImplemented("This functionality has not implemented")
