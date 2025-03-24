import pytest

from src.problems.binary_search.time_based_key_value_store.script import TimeMap


def test_time_map():
    time_map = TimeMap()

    # Test case 1: Setting and getting values
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"  # Exact match
    assert time_map.get("foo", 3) == "bar"  # Latest before 3

    # Test case 2: Overwriting values at a later timestamp
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"  # Exact match
    assert time_map.get("foo", 5) == "bar2"  # Latest before 5

    # Test case 3: Key that does not exist
    assert time_map.get("bar", 1) == ""  # No such key

    # Test case 4: Timestamp before any set time
    assert time_map.get("foo", 0) == ""  # No earlier value

    # Test case 5: Multiple values for the same key
    time_map.set("key1", "value1", 10)
    time_map.set("key1", "value2", 20)
    time_map.set("key1", "value3", 30)

    assert time_map.get("key1", 5) == ""  # No values before 10
    assert time_map.get("key1", 10) == "value1"  # Exact match
    assert time_map.get("key1", 15) == "value1"  # Latest before 15
    assert time_map.get("key1", 20) == "value2"  # Exact match
    assert time_map.get("key1", 25) == "value2"  # Latest before 25
    assert time_map.get("key1", 30) == "value3"  # Exact match
    assert time_map.get("key1", 35) == "value3"  # Latest before 35

    # Test case 6: Large timestamps
    time_map.set("bigkey", "bigval1", 1000000)
    time_map.set("bigkey", "bigval2", 2000000)
    assert time_map.get("bigkey", 1500000) == "bigval1"  # Latest before 1500000
    assert time_map.get("bigkey", 2500000) == "bigval2"  # Latest before 2500000


if __name__ == "__main__":
    pytest.main()
