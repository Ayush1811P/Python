        #BUGGY CODE

def binary_search(arr, target):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target > mid:
            low = mid + 1
        else:
            high = mid - 1

    return -1



        #FIXED CODE


def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1        