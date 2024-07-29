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


