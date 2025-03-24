def partition(arr: list[int], low: int, high: int) -> int:
    # Last element as pivot, incase of reverse sorted array this
    # will lead to O(n^2) time complexity. Else it will be O(nlogn)

    pivot = arr[high]
    idx = low - 1

    for i in range(low, high):
        if arr[i] < pivot:
            idx += 1
            tmp = arr[idx]
            arr[idx] = arr[i]
            arr[i] = tmp

    idx += 1
    arr[high] = arr[idx]
    arr[idx] = pivot

    return idx


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_idx = partition(arr, low, high)
    quick_sort(arr, low, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, high)
