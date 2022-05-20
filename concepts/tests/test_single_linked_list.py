import pytest 
from data_structures.single_linked_list import SingleLinkedList

@pytest.fixture
def ex_list():
    return SingleLinkedList([1, 2, 3, 4, 5])

@pytest.mark.parametrize("key, expected", [
    (1, [2, 3, 4, 5]),
    (3, [1, 2, 4, 5]),
    (5, [1, 2, 3, 4]),
])
def test_delete_key(ex_list, key, expected):
    ex_list.delete_key(key)
    res = ex_list.get_as_list()
    assert res == expected
