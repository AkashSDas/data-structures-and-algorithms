import pytest

from src.problems.arrays_and_hashing.encode_decode_strings.script import decode, encode


@pytest.mark.parametrize(
    "input_data, expected_encoded",
    [
        (
            ["Hello", "World"],
            "5:Hello5:World",
        ),  # Encode and decode a simple string array
        ([], ""),  # Encode and decode an empty string array
        (["OpenAI"], "6:OpenAI"),  # Encode and decode a single-word string
        (["A"], "1:A"),  # Encode and decode a single-character string
    ],
)
def test_encode_decode(input_data, expected_encoded):
    encoded = encode(input_data)
    decoded = decode(encoded)

    assert encoded == expected_encoded
    assert decoded == input_data


# Uncomment this test if the `decode` function is expected to return an empty list for invalid input
# def test_decode_invalid_input():
#     invalid_input = "InvalidInput"
#     decoded = decode(invalid_input)
#     assert decoded == []


def test_encode_decode_large_string_array():
    large_input = [f"Word{i}" for i in range(1000)]

    import time

    start_time = time.time()
    encoded = encode(large_input)
    decoded = decode(encoded)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds

    assert elapsed_time < 10  # Ensure it completes within 10ms
    assert decoded == large_input
