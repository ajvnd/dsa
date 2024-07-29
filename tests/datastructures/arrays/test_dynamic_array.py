import pytest

from src.datastructures.arrays.dynamic_array import DynamicArray


class TestDynamicArray():

    @pytest.fixture
    def dynamic_array(self):
        return DynamicArray(int)

    def test_can_initialize_fields_correctly(self, dynamic_array):
        # arrange

        # act

        # assert
        assert isinstance(dynamic_array, DynamicArray)
        assert dynamic_array._capacity == 2
        assert dynamic_array.__dict__['_StaticArray__item_type'] == int

    def test_raise_exception_if_item_type_is_not_primitive(self):
        # arrange

        # act and assert
        with pytest.raises(TypeError):
            DynamicArray(type)

    def test_raise_exception_if_tried_to_access_invalid_index(self, dynamic_array):
        # arrange
        new_item = 5

        # act & assert

        with pytest.raises(IndexError):
            dynamic_array[3] = new_item

    @pytest.mark.parametrize("index", [(0), (1)])
    def test_can_set_items_correctly(self, index, dynamic_array):
        # arrange
        new_item = 5

        # act
        dynamic_array[index] = new_item

        # assert
        assert dynamic_array[index] == new_item

    def test_raise_exception_if_an_inconsistent_type_is_set(self, dynamic_array):
        # arrange
        new_item = 'five'

        # act and assert
        with pytest.raises(TypeError):
            dynamic_array[0] = new_item

    def test_can_get_items_correctly(self, dynamic_array):
        # arrange
        new_item = 5

        # act
        dynamic_array[0] = new_item
        dynamic_array[1] = new_item + 1

        # assert
        assert dynamic_array[0] == new_item
        assert dynamic_array[1] == new_item + 1

    def test_can_delete_items_correctly(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5

        # act
        del dynamic_array[0]

        # assert
        assert dynamic_array[0] is None

    def test_can_shift_if_array_has_more_than_one_items_when_deletion(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array[1] = 6

        # act
        del dynamic_array[0]

        # assert
        assert dynamic_array[0] == 6

    def test_can_hold_if_array_has_more_than_one_items_and_last_item_deleted(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array[1] = 6

        # act
        del dynamic_array[1]

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] is None