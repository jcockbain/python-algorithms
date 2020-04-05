def binary_search(arr, low, high, target):
    while low < high:
        mid = (low + (high - 1)) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
    return -1
