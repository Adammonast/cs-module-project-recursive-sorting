# TO-DO: complete the helper function below to merge 2 sorted arrays
# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)

    # making an array of 0s that is the length of the integer
    merged_arr = [0] * elements

    a = 0  # index for arrA
    b = 0  # index for arrB
    i = 0  # incremented index

    # while length of arrA is greater than i and length of arrB is greater than j
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            # a is smaller, it should be added next
            merged_arr[i] = arrA[a]
            # increment arrA's index
            a += 1
        else:
            # b is smaller, should be added next
            merged_arr[i] = arrB[b]
            # increment arrB's index
            b += 1

        i += 1
    # while individual arrs are greater than index
    while a < len(arrA):
        merged_arr[i] = arrA[a]
        a += 1
        i += 1

    while b < len(arrB):
        merged_arr[i] = arrB[b]
        b += 1
        i += 1

    # Your code here

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    # base, stop reducing in half here
    if len(arr) <= 1:
        return arr

    # reducing down by half until each list has 1 sorted item
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursive dividing on the subarrays until each only has 1 element remaining
    left = merge_sort(left)
    right = merge_sort(right)

    # compare/merge the 1 sorted item in each subarray
    arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
