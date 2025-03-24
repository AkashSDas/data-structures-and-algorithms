def counting_sort(arr: list[int]) -> None:
    if len(arr) == 0:
        return

    max_num = max(arr)
    count_arr = [0] * (max_num + 1)

    for num in arr:
        count_arr[num] += 1

    update_count = 0
    for idx in range(len(count_arr)):
        while count_arr[idx] > 0:
            arr[update_count] = idx
            update_count += 1
            count_arr[idx] -= 1
