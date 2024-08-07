import pytest

from src.datastructures.linkedlists.singly_linkedlist import SinglyLinkedList


class TestABC:

    @pytest.fixture
    def singly_linkedlist(self):
        return SinglyLinkedList()
    def test_init_initialize_fields_2(self, singly_linkedlist):
        pass
        # arrange

        # act

        # assert
