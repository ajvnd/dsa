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
        assert dynamic_array._capacity == 1
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
            dynamic_array[2] = new_item

    def test_can_set_items_correctly(self, dynamic_array):
        # arrange
        new_item = 5

        # act
        dynamic_array[0] = new_item

        # assert
        assert dynamic_array[0] == new_item

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

        # assert
        assert dynamic_array[0] == new_item

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
        dynamic_array.append(6)

        # act
        del dynamic_array[0]

        # assert
        assert dynamic_array[0] == 6

    def test_can_hold_if_array_has_more_than_one_items_and_last_item_deleted(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)

        # act
        del dynamic_array[1]

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] is None

    def test_can_remove_an_item(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)
        # act
        dynamic_array.remove(5)

        # assert
        assert dynamic_array[0] == 6
        assert dynamic_array[1] is None

    def test_can_represent_items_correctly(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5

        # act
        items = str(dynamic_array)

        # assert
        assert isinstance(items, str)
        assert 'DynamicArray([5])' == str(dynamic_array)

    def test_can_return_correct_length(self, dynamic_array):
        # arrange
        new_item = 5

        # act
        dynamic_array[0] = new_item
        dynamic_array.append(new_item + 1)

        # assert
        assert len(dynamic_array) == 2

    def test_can_get_index_of_items_correctly(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5

        # act
        index = dynamic_array.get_index(5)

        # assert
        assert index == 0

    def test_can_reverse_items_correctly(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)
        dynamic_array.append(7)
        dynamic_array.append(8)
        dynamic_array.append(9)

        # act
        dynamic_array.reverse()

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] == 6
        assert dynamic_array[2] == 7
        assert dynamic_array[3] == 8
        assert dynamic_array[4] == 9
        assert dynamic_array[5] is None