def insertion_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
