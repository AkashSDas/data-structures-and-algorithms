from src.problems.linked_list.lru_cache.script import LRUCache


def test_example_case():
    lru_cache = LRUCache(2)

    lru_cache.put(1, 1)  # cache is {1=1}
    lru_cache.put(2, 2)  # cache is {1=1, 2=2}
    assert lru_cache.get(1) == 1  # returns 1
    lru_cache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
    assert lru_cache.get(2) == -1  # returns -1 (not found)
    lru_cache.put(4, 4)  # evicts key 1, cache is {4=4, 3=3}
    assert lru_cache.get(1) == -1  # returns -1 (not found)
    assert lru_cache.get(3) == 3  # returns 3
    assert lru_cache.get(4) == 4  # returns 4


def test_update_existing_key():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(1, 10)  # Update key 1
    assert lru_cache.get(1) == 10
    lru_cache.put(3, 3)  # evicts key 2
    assert lru_cache.get(2) == -1
    assert lru_cache.get(3) == 3


def test_single_element_cache():
    lru_cache = LRUCache(1)
    lru_cache.put(1, 1)
    assert lru_cache.get(1) == 1
    lru_cache.put(2, 2)  #
