import pytest

from src.datastructures.linkedlists.singly_linkedlist import SinglyLinkedList


class TestABC:

    @pytest.fixture
    def singly_linkedlist(self):
        return SinglyLinkedList()


    def test_init_initialize_fields(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        assert singly_linkedlist.head is None
        assert singly_linkedlist.tail is None

    def test_add_inserts_item_at_head_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_first(4)

        # assert
        assert singly_linkedlist.head.data == 4
        assert singly_linkedlist.tail.data == 4

    def test_add_inserts_at_head_and_shifts_existing_node_when_linkedlist_is_not_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_first(4)
        singly_linkedlist.add_first(5)

        # assert
        assert singly_linkedlist.head.data == 5
        assert singly_linkedlist.head.next == singly_linkedlist.tail
        assert singly_linkedlist.head.next.data == 4


