import pytest

from src.datastructures.arrays.dynamic_array import DynamicArray


class TestDynamicArray():

    @pytest.fixture
    def dynamic_array(self):
        return DynamicArray(int)

    def test_append_stores_item_at_end(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5

        # act
        dynamic_array.append(6)

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] == 6

    def test_insert_adds_item_at_end_without_shift(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5

        # act
        dynamic_array.insert(1, 6)

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] == 6

    def test_insert_inserts_items_in_middle_and_shifts_right(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)
        dynamic_array.append(7)

        # act
        dynamic_array.insert(1, 1)

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] == 1
        assert dynamic_array[2] == 6
        assert dynamic_array[3] == 7

    def test_remove_removes_items(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)

        # act
        dynamic_array.remove(5)

        # assert
        assert dynamic_array[0] == 6
        assert dynamic_array[1] is None

    def test_delitem_removes_items_and_shifts_elements(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)

        # act
        del dynamic_array[0]

        # assert
        assert dynamic_array[0] == 6

    def test_delitem_removes_last_item_without_shifting(self, dynamic_array):
        # arrange
        dynamic_array[0] = 5
        dynamic_array.append(6)

        # act
        del dynamic_array[1]

        # assert
        assert dynamic_array[0] == 5
        assert dynamic_array[1] is None
