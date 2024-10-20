import pytest

from src.datastructures.linkedlists.common.empty_linkedlist_exception import EmptyLinkedListException
from src.datastructures.linkedlists.singly_linkedlist import SinglyLinkedList


class TestSinglyLinedList:

    @pytest.fixture
    def singly_linkedlist(self):
        return SinglyLinkedList()

    def test_init_initialize_fields(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        assert singly_linkedlist.head is None
        assert singly_linkedlist.tail is None

    def test_add_first_inserts_at_head_and_tail_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_first(4)

        # assert
        assert singly_linkedlist.head.data == 4
        assert singly_linkedlist.head == singly_linkedlist.tail

    def test_add_first_inserts_at_head_and_shifts_existing_nodes(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_first(4)
        singly_linkedlist.add_first(5)

        # assert
        assert singly_linkedlist.head.data == 5
        assert singly_linkedlist.tail.data == 4

    def test_add_last_inserts_at_head_and_tail_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_last(4)

        # assert
        assert singly_linkedlist.head.data == 4
        assert singly_linkedlist.head == singly_linkedlist.tail

    def test_add_last_inserts_last_and_shift_existing_nodes(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_last(4)
        singly_linkedlist.add_last(5)

        # assert
        assert singly_linkedlist.tail.data == 5
        assert singly_linkedlist.head.data == 4

    def test_add_at_raises_exception_when_access_invalid_index(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(IndexError):
            singly_linkedlist.add_at(1, 4)

    def test_add_at_inserts_add_head_and_tail_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act
        singly_linkedlist.add_at(0, 4)

        # assert
        assert singly_linkedlist.head.data == 4
        assert singly_linkedlist.tail == singly_linkedlist.head

    @pytest.mark.parametrize('index', [(0), (1), (2), (3)])
    def test_add_at_inserts_at_specific_index(self, index, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_first(1)
        singly_linkedlist.add_first(2)
        singly_linkedlist.add_first(3)
        singly_linkedlist.add_first(4)

        # act
        singly_linkedlist.add_at(index, 5)

        # assert
        assert singly_linkedlist._getitem(index).data == 5

    def test_remove_first_raises_exception_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(EmptyLinkedListException):
            singly_linkedlist.remove_first()

    def test_remove_deletes_head(self, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_first(4)
        singly_linkedlist.add_first(5)

        # act
        singly_linkedlist.remove_first()

        # assert
        assert singly_linkedlist.head.data == 4
        assert singly_linkedlist.head == singly_linkedlist.tail

    def test_remove_last_raises_exception_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(EmptyLinkedListException):
            singly_linkedlist.remove_last()

    def test_remove_last_removes_head_and_tail_with_one_item(self, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_last(4)

        # act
        singly_linkedlist.remove_last()

        # assert

        assert singly_linkedlist.head is None
        assert singly_linkedlist.tail is None

    def test_remove_last_deletes_last_and_set_tail_previous_to_last(self, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_last(4)
        singly_linkedlist.add_last(5)

        # act
        singly_linkedlist.remove_last()

        # assert

        assert singly_linkedlist.head.data == 4
        assert singly_linkedlist.head == singly_linkedlist.tail

    def test_remove_at_raises_exception_when_access_invalid_index(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(IndexError):
            singly_linkedlist.remove_at(1)


    def test_remove_at_raises_exception_when_linklist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(EmptyLinkedListException):
            singly_linkedlist.remove_at(0)

    @pytest.mark.parametrize('index', [(0), (1), (2), (3)])
    def test_remove_at_deletes_at_specific_index(self, index, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_first(3)
        singly_linkedlist.add_first(2)
        singly_linkedlist.add_first(1)
        singly_linkedlist.add_first(0)

        # act
        singly_linkedlist.remove_at(index)

        # assert
        if index + 1 <= len(singly_linkedlist):
            assert singly_linkedlist._getitem(index).data == index + 1
        else:
            with pytest.raises(IndexError):
                assert singly_linkedlist._getitem(index).data == None

    def test_peak_first_raises_exception_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(EmptyLinkedListException):
            singly_linkedlist.peak_first()

    def test_peak_first_returns_head(self, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_first(1)
        singly_linkedlist.add_first(2)

        # act
        head = singly_linkedlist.peak_first()

        # assert
        assert head.data == 2

    def test_peak_last_raises_exception_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        with pytest.raises(EmptyLinkedListException):
            singly_linkedlist.peak_last()


    def test_peak_last_returns_head(self, singly_linkedlist: SinglyLinkedList):
        # arrange
        singly_linkedlist.add_first(1)
        singly_linkedlist.add_first(2)

        # act
        tail = singly_linkedlist.peak_last()

        # assert
        assert tail.data == 1

    def test_repr_returns_empty_list_when_linkedlist_is_empty(self, singly_linkedlist: SinglyLinkedList):
        # arrange

        # act

        # assert
        assert str(singly_linkedlist) == "Empty LinkedList"
