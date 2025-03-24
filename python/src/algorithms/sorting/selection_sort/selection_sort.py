def selection_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp
