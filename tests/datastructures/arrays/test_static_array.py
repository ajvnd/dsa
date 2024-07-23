import pytest

from src.datastructures.arrays.static_array import StaticArray


class TestStaticArray:

    @pytest.fixture
    def static_array(self):
        return StaticArray(int, 5)

    def test_can_initialize_fields_correctly(self, static_array):
        # arrange

        # act

        # assert
        assert isinstance(static_array, StaticArray)
        assert static_array._capacity == 5
        assert static_array.__dict__['_StaticArray__item_type'] == int

    def test_raise_exception_if_capacity_less_than_zero(self, static_array):
        # arrange
        type = None
        capacity = -1

        # act and assert
        with pytest.raises(ValueError):
            StaticArray(type, capacity)

    def test_raise_exception_if_item_type_is_not_primitive(self, static_array):
        # arrange
        type = None
        capacity = 5

        # act and assert
        with pytest.raises(TypeError):
            StaticArray(type, capacity)

    def test_can_set_items_correctly(self, static_array):
        # arrange
        new_item = 5

        # act
        static_array[0] = new_item

        # assert
        assert static_array[0] == new_item

    def test_can_get_items_correctly(self, static_array):
        # arrange
        new_item = 5

        # act
        static_array[0] = new_item

        # assert
        assert static_array[0] == new_item

    def test_can_delete_items_correctly(self, static_array):
        # arrange
        new_item = 5
        static_array[0] = new_item

        # act
        del static_array[0]

        # assert
        assert static_array[0] == None
