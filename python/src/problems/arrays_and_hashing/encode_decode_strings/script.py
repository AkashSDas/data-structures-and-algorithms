# Encode and decode a string. Don't maintain any state.
# Input - ["Hello", "World"]
# Output - ["Hello", "World"]
# Encode - "5:Hello5:World"


def encode(text: list[str]) -> str:
    result = ""

    for word in text:
        result += f"{len(word)}:{word}"

    return result


def decode(val: str) -> list[str]:
    result: list[str] = []

    last_idx = 0
    curr_idx = 0

    while curr_idx < len(val):
        if val[curr_idx] == ":":
            str_len = int(val[last_idx:curr_idx])
            word = val[curr_idx + 1 : curr_idx + 1 + str_len]
            result.append(word)
            last_idx = curr_idx + str_len + 1
            curr_idx = curr_idx + str_len + 1
        else:
            curr_idx += 1

    return result
